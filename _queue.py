from collections import deque
from typing import Any


class Queue(object):
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)

    def reverse(self) -> None:
        queue = []
        while self.queue:
            queue.append(self.queue.pop())
        [self.queue.append(d) ]
        self.queue = queue


if __name__ == "__main__":
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    print(q.popleft())
    print("--------------------------")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue.queue)
    queue.reverse()
    print(queue.queue)