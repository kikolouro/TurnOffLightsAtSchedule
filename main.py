import os
import asyncio
from xknx import XKNX
from xknx.devices import Light
from xknx.core import ValueReader
from xknx.telegram import GroupAddress


def getGroupAddresses():
    groupAddresses = []
    for var in os.environ:
        if var.startswith('light'):
            groupAddresses.append(os.environ[var])
    # print(groupAddresses)
    return groupAddresses


async def main():
    xknx = XKNX()
    await xknx.start()
    groupAddresses = getGroupAddresses()
    for groupAddress in groupAddresses:

        light = Light(xknx,
                      name='HelloWorldLight',
                      group_address_switch=f"{groupAddress}")
        await light.sync(wait_for_result=True)
        await light.set_off()

    await xknx.stop()

# getGroupAddresses()
asyncio.run(main())
