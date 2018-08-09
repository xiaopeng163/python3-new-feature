import time
from datetime import datetime


def print_message_periodical(interval_seconds, message='keep alive'):
    while True:
        print(f'{datetime.now()} - {message}')
        start = time.time()
        end = start + interval_seconds
        while True:
            yield
            now = time.time()
            if now >= end:
                break