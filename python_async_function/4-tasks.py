#!/usr/bin/env python3
"""Execute multiple asyncio tasks concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run n tasks and return their delays in completion order."""
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
