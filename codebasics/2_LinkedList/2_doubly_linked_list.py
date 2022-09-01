class Node:
  def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    return count

  def print_forward(self):
    if self.head is None:
      print("LinkedList is empty")
      return
    
    itr = self.head
    llstr = ''

    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next

    print(llstr)

  def get_tail(self):
    itr = self.head
    while itr.next:
      itr=itr.next
    return itr

  def print_backward(self):
    if self.head is None:
      print("LinkedList is empty")
      return

    tail = self.get_tail()
    itr = tail
    llstr=''
    while itr:
      llstr += itr.data + '-->'
      itr = itr.prev
    print(llstr)

  def insert_at_begining(self, data):
    
    node = Node(data, self.head, None)
    self.head.prev = node
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None, None)
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next

    itr.next = Node(data, None, itr)


  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data) 

  def insert_at(self, index, data):
    if index < 0 or index > self.get_length():
      raise Exception("Invalid Index")
    
    if index == 0:
      self.insert_at_begining(data)
      return
    
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        node = Node(data, itr.next, itr)
        if itr.next is not None:
          itr.next.prev = node
        itr.next = node
        break
      
      itr = itr.next
      count += 1

  def remove_at(self, index):
    if index < 0 or index >= self.get_length():
      raise Exception("Invalid index")

    if index == 0:
      self.head = self.head.next
      return

    itr = self.head
    count = 0
    while itr:
      if count == index - 1:
        itr.next = itr.next.next
      count += 1
      itr = itr.next
    
if __name__ == "__main__":
  ll = DoublyLinkedList()
  ll.insert_values(["banana","mango","grapes","orange"])
  # ll.print_forward()
  ll.print_backward()
  ll.insert_at_end("figs")
  # ll.print_forward()
  ll.print_backward()
  ll.insert_at(0,"jackfruit")
  # ll.print_forward()
  ll.print_backward()
  ll.insert_at(6,"dates")
  # ll.print_forward()
  ll.print_backward()
  ll.insert_at(2,"kiwi")
  # ll.print_forward()
  ll.print_backward()
