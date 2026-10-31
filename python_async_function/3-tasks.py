#!/usr/bin/env python3
"""Create an asyncio Task for a random delay coroutine."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return a Task that runs wait_random."""
    return asyncio.create_task(wait_random(max_delay))
