# xKNX stuff
import os
import asyncio
from xknx import XKNX
from xknx.devices import Light
from xknx.core import ValueReader
from xknx.io import GatewayScanner, UDPTunnel
from xknx.telegram import GroupAddress, IndividualAddress, Telegram
from xknx.telegram.apci import GroupValueWrite
from xknx.dpt import DPTBinary

# Logging stuff
import logging
logging.basicConfig(filename="/logs/lights_shutdown.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a', level=logging.INFO)


def getGroupAddresses():
    groupAddresses = []
    for var in os.environ:
        if var.startswith('light'):
            groupAddresses.append(os.environ[var])
    return groupAddresses


async def main():
    xknx = XKNX()
    gatewayscanner = GatewayScanner(xknx)
    gateways = await gatewayscanner.scan()
    if not gateways:
        logging.error("No Gateways found")
        return

    groupAddresses = getGroupAddresses()
    for groupAddress in groupAddresses:
        logging.info(f"[{groupAddress}] - Starting Process ")
        await xknx.start()
        for gateway in gateways:
            logging.info(
                f"[{groupAddress}] - Connecting to {gateway.name} using IP {gateway.ip_addr}")
            tunnel = UDPTunnel(
                xknx,
                gateway_ip=gateway.ip_addr,
                gateway_port=gateway.port,
                local_ip=gateway.local_ip,
                local_port=0,
                route_back=False,
            )
            await tunnel.connect()
            await tunnel.send_telegram(
                Telegram(
                    destination_address=GroupAddress(f"{groupAddress}"),
                    payload=GroupValueWrite(DPTBinary(0)),
                )
            )
            await tunnel.disconnect()
            logging.info(
                f"[{groupAddress}] - Disconnected from {gateway.name}")
        await xknx.stop()
        logging.info(f"[{groupAddress}] - Ended Process ")
asyncio.run(main())
