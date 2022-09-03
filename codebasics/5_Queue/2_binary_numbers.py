from collections import deque
class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()

  def front(self):
    return self.buffer[-1]

  def is_empty(self):
    return len(self.buffer) == 0

  def size(self):
    return len(self.buffer)

def print_binary(c):
  q.enqueue(1)
  while not q.is_empty() and c:
    n = q.dequeue()
    print(n)
    q.enqueue(int(str(n) + "0"))
    q.enqueue(int(str(n) + "1"))
    c -= 1

if __name__ == "__main__":
  q = Queue()
  print_binary(10)
