from async_search import async_search
from async_print import print_message_periodical
from async_search_prime import async_search_prime
from task import Scheduler


def main():
    scheduler = Scheduler()
    scheduler.add(async_search(3))
    scheduler.add(async_search(4))
    scheduler.add(print_message_periodical(3))
    scheduler.add(async_search_prime())
    scheduler.run_to_completion()

if __name__ == "__main__":
    main()
