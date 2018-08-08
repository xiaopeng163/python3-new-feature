import time
from datetime import datetime
from queue import deque


def search(n):
    a,b = 0, 1
    while True:
        if len(str(a)) >= n:
            return a
        yield
        a, b = b, a + b

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


class Task:

    next_id = 0

    def __init__(self, routine):
        self.id = Task.next_id
        Task.next_id += 1
        self.routine = routine


class Scheduler:

    def __init__(self):
        self.runnable_tasks = deque()
        self.completed_task_results = {}
        self.failed_task_errors = {}
    
    def add(self, routine):
        task = Task(routine)
        self.runnable_tasks.append(task)
        return task.id
    
    def run_to_completion(self):
        while len(self.runnable_tasks) !=0:
            task = self.runnable_tasks.popleft()
            # print(f"Running task {task.id} ...", end='')
            try:
                yielded = next(task.routine)
            except StopIteration as stopped:
                print(f'completed with result: {stopped.value}')
                self.completed_task_results[task.id] = stopped.value
            except Exception as e:
                print(f'failed with exception: {e}')
                self.failed_task_errors[task.id] = e
            else:
                assert yielded is None
                # print('now yieldedd')
                self.runnable_tasks.append(task)


if __name__ == "__main__":
    t = time.time()
    scheduler = Scheduler()
    scheduler.add(print_message_periodical(3))
    scheduler.add(search(300))
    scheduler.add(search(400))
    scheduler.run_to_completion()
    print(f'time: {time.time() - t}')