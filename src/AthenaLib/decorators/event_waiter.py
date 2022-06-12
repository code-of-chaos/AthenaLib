# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def event_waiter(coroutine):
    loop = asyncio.new_event_loop()
    async def wrapper(event:asyncio.Event, *args, **kwargs):
        await event.wait()
        print("called")
        return await coroutine(*args, **kwargs)
    return lambda *args, **kwargs: loop.run_until_complete(wrapper(*args, **kwargs))