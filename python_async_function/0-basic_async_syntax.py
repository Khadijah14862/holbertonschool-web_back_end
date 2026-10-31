#!/usr/bin/env python3
"""Define a coroutine that waits for a random delay."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the delay in seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
