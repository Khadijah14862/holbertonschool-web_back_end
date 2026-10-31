#!/usr/bin/env python3
"""Collect random numbers using asynchronous comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return ten random numbers from an async generator."""
    return [number async for number in async_generator()]
