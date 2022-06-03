import os
import asyncio
from xknx import XKNX
from xknx.devices import Light
from xknx.core import ValueReader
from xknx.telegram import GroupAddress



async def main():
    xknx = XKNX()
    await xknx.start()
    light = Light(xknx,
                  name='HelloWorldLight',
                  group_address_switch=f"{os.environ['light']}")
    await light.sync(wait_for_result=True)
    await light.set_off()
    await asyncio.sleep(1)
    await light.sync(wait_for_result=True)
    await xknx.stop()

asyncio.run(main())
