from collections import deque
import threading
import time

class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()

  def is_empty(self):
    return len(self.buffer) == 0

  def size(self):
    return len(self.buffer)

def place_order(orders):
  for order in orders:
    order_queue.enqueue(order)
    time.sleep(0.5)

def server_order():
  time.sleep(1)
  while not order_queue.is_empty():
    print(order_queue.dequeue())
    time.sleep(2)

if __name__ == "__main__":
  order_queue = Queue()
  orders = ['pizza','samosa','pasta','biryani','burger']

  place = threading.Thread(target=place_order, args=(orders, )) # t1
  serve = threading.Thread(target=server_order) # t2
  t = time.time()
  # place_order(orders)
  # server_order()
  place.start()
  serve.start()
  place.join()
  serve.join()

  print(time.time() - t)