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
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
async def _request(
        headers:dict, url:str, data:bytes=None, query_parameters:dict=None,
        *, loop:asyncio.AbstractEventLoop=None, method:str
):
    if loop is None:
        loop = asyncio.get_running_loop()

    # assemble the request
    req = urllib.request.Request(
        f"{url}?{urllib.parse.urlencode(query_parameters)}" if query_parameters is not None or query_parameters else url,
        headers=headers,
        method=method,
    )

    # run the request
    return await loop.run_in_executor(
        executor=None,
        func=lambda: urllib.request.urlopen(req,data=data)
    )
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def get(
        headers:dict,url:str,data:bytes=None,query_parameters:dict=None,
        *,loop:asyncio.AbstractEventLoop=None
):
    return await _request(
        headers=headers,
        url=url,
        data=data,
        query_parameters=query_parameters,
        loop=loop,
        method="GET"
    )

async def post(
        headers:dict,url:str,data:bytes=None,query_parameters:dict=None,
        *, loop:asyncio.AbstractEventLoop=None
):
    return await _request(
        headers=headers,
        url=url,
        data=data,
        query_parameters=query_parameters,
        loop=loop,
        method="POST"
    )

async def patch(
        headers:dict,url:str,data:bytes=None,query_parameters:dict=None,
        *,loop:asyncio.AbstractEventLoop=None
):
    return await _request(
        headers=headers,
        url=url,
        data=data,
        query_parameters=query_parameters,
        loop=loop,
        method="PATCH"
    )

async def delete(
        headers:dict,url:str,data:bytes=None,query_parameters:dict=None,
        *, loop:asyncio.AbstractEventLoop=None
):
    return await _request(
        headers=headers,
        url=url,
        data=data,
        query_parameters=query_parameters,
        loop=loop,
        method="DELETE"
    )