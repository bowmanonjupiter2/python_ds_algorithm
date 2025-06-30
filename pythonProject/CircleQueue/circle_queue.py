import threading


class CircleQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0
        self.lock = threading.Lock()

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def enqueue(self, item):
        with self.lock:
            if self.is_full():
                raise OverflowError("queue full")
            else:
                self.queue[self.rear] = item
                self.rear = (self.rear + 1) % self.size
                self.count += 1

    def dequeue(self):
        with self.lock:
            if self.is_empty():
                raise IndexError("Queue is empty")
            else:
                item = self.queue[self.front]
                self.queue[self.front] = None
                self.front = (self.front + 1) % self.size
                self.count -= 1
                return item


def test_circle_queue_1():
    queue = CircleQueue(5)

    try:

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        queue.enqueue(6)

    except Exception as e:
        print(f"Expected error: {e}")


def test_circle_queue_2():
    queue = CircleQueue(5)

    try:

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

        queue.dequeue()

    except Exception as e:
        print(f"Expected error: {e}")


def main():
    test_circle_queue_1()
    test_circle_queue_2()


if __name__ == "__main__":
    main()
