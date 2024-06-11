#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from typing import Generator
import random


async def async_generator():
    """Async Generator that loops 10 times,
    each time asynchronously waits 1
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
