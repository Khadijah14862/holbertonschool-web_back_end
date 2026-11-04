#!/usr/bin/env python3
"""Measure the runtime of four concurrent comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Measure the execution time of four concurrent comprehensions."""
    start = time.perf_counter()

    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    end = time.perf_counter()
    return end - start
