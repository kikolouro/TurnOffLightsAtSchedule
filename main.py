import os
import asyncio
from xknx import XKNX
from xknx.devices import Light
from xknx.core import ValueReader
from xknx.io import GatewayScanner, UDPTunnel
from xknx.telegram import GroupAddress, IndividualAddress, Telegram
from xknx.telegram.apci import GroupValueWrite
from xknx.dpt import DPTBinary


def getGroupAddresses():
    groupAddresses = []
    for var in os.environ:
        if var.startswith('light'):
            groupAddresses.append(os.environ[var])
    print(groupAddresses)
    return groupAddresses


async def main():
    xknx = XKNX()
    gatewayscanner = GatewayScanner(xknx)
    gateways = await gatewayscanner.scan()
    groupAddresses = getGroupAddresses()
    for groupAddress in groupAddresses:
        await xknx.start()
        if not gateways:
            print("No Gateways found")
            return
        for gateway in gateways:
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

        await xknx.stop()
        await tunnel.disconnect()
# getGroupAddresses()
asyncio.run(main())
