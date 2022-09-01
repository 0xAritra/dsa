class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count += 1
      itr = itr.next
    return count

  def print(self):
    if self.head is None:
      print("LinkedList is empty")
      return
    
    itr = self.head
    llstr = ''

    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next

    print(llstr)

  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next

    itr.next = Node(data, None)

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
        node = Node(data, itr.next)
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
  ll = LinkedList()
  
  # ll.insert_at_begining(10)
  # ll.insert_at_begining(20)

  # ll.insert_at_end(10)
  # ll.insert_at_end(20)
  # ll.insert_at_end(30)

  ll.insert_values(["banana", "apple", "orange", "mango"])

  ll.print()
  print("length:", ll.get_length())

  ll.remove_at(0)
  ll.insert_at(0, "figs")
  ll.insert_at(3, "jackfruit")
  ll.print()

  ll.insert_values([56, 21, 198, 44, 65])
  ll.insert_at(0, 10)
  ll.insert_at(4, 70)
  print("length:", ll.get_length())

  ll.print()
