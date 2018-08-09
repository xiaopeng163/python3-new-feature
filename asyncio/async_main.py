import asyncio
import time
from math import sqrt
from datetime import datetime


# def async_search(n):
#     a, b = 0, 1
#     while True:
#         if len(str(a)) >= n:
#             return a
#         yield
#         a, b = b, a + b

async def search(n):
    a, b = 0, 1
    while True:
        if len(str(a)) >= n:
            print(a)
            return
        await asyncio.sleep(0)
        a, b = b, a + b


async def print_message_periodical(interval_seconds, message='keep alive'):
    while True:
        print(f'{datetime.now()} - {message}')
        start = time.time()
        end = start + interval_seconds
        while True:
            await asyncio.sleep(0)
            now = time.time()
            if now >= end:
                break

async def search_prime():
    a, b = 0, 1
    while True:
        result = await is_prime(a)
        if result:
            print(f'found: {a}')
        a, b = b, a + b


async def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
        await asyncio.sleep(0)
    return True


if __name__ == "__main__":
    try:
        scheduler = asyncio.get_event_loop()
        scheduler.create_task(
            print_message_periodical(3)
        )
        scheduler.create_task(search(1000))
        scheduler.create_task(search_prime())
        scheduler.run_forever()
    except KeyboardInterrupt:
        scheduler.stop()
        scheduler.close()