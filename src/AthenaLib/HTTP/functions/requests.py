# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import urllib.request
import urllib.parse
import asyncio

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def get(headers:dict,url:str,query_parameters:dict=None,*, loop:asyncio.AbstractEventLoop=None):
    if loop is None:
        loop = asyncio.get_running_loop()

    # assemble the request
    req = urllib.request.Request(
        f"{url}?{urllib.parse.urlencode(query_parameters)}" if query_parameters is not None else url,
        headers=headers,
    )

    # run the request
    return await loop.run_in_executor(
        executor=None,
        func=lambda: urllib.request.urlopen(req)
    )

async def post(headers:dict,url:str,data:bytes,query_parameters:dict=None, *, loop:asyncio.AbstractEventLoop=None):
    if loop is None:
        loop = asyncio.get_running_loop()

    # assemble the request
    req = urllib.request.Request(
        f"{url}?{urllib.parse.urlencode(query_parameters)}" if query_parameters is not None else url,
        headers=headers,
        method="POST",
    )

    # run the request
    return await loop.run_in_executor(
        executor=None,
        func=lambda: urllib.request.urlopen(req,data)
    )