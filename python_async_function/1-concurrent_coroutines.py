#!/usr/bin/env python3
"""Execute multiple asynchronous coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return delays in completion order."""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
