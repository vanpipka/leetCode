class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:

        if len(self.queue) == 0:
            return None

        result = self.queue[0]

        self.queue = self.queue[1:]

        return result

    def peek(self) -> int:

        if len(self.queue) == 0:
            return None

        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

def main():

    my_queue = MyQueue()
    my_queue.push(1) # queue is: [1]
    my_queue.push(2) # queue is: [1, 2](leftmost is front of the queue)
    my_queue.peek() # return 1
    my_queue.pop() # return 1, queue is [2]
    my_queue.empty() # return false

    return []

def test():
    assert main() == []
