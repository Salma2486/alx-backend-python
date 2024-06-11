#!/usr/bin/env python3
"""1-async_comprehension.py"""
import asyncio
import random
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """The coroutine will collect 10 random numbers using an async
    generator and return them.
    """
    return [i async for i in async_generator()]
