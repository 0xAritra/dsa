class BinarySearchTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, val):
    if val == self.data:
      return

    elif val < self.data:
      if self.left:
        self.left.add_child(val)
      else:
        self.left = BinarySearchTreeNode(val)

    else:
      if self.right:
        self.right.add_child(val)
      else:
        self.right = BinarySearchTreeNode(val)

  def search(self, val):
    if self.data == val:
      return True

    elif val < self.data:
      if self.left:
        return self.left.search(val)
      else:
        return False

    else:
      if self.right:
        return self.right.search(val)
      else:
        return False

  def in_order_traversal(self):
    el = []
    if self.left:
      el += self.left.in_order_traversal()

    el.append(self.data)

    if self.right:
      el += self.right.in_order_traversal()

    return el

  def calculate_sum(self):
    # return sum(self.in_order_traversal())
    sum = self.data
    if self.left:
      sum += self.left.calculate_sum()
    if self.right:
      sum += self.right.calculate_sum()
    return sum

  def find_min(self):
    # return min(self.in_order_traversal())

    # itr = self
    # while itr.left:
    #   itr = itr.left
    # return itr.data

    if self.left:
      return self.left.find_min()
    return self.data

  def find_max(self):
    if self.right:
      return self.right.find_max()
    return self.data

  def pre_order_traversal(self):
    el = []
    el.append(self.data)

    if self.left:
      el += self.left.pre_order_traversal()

    if self.right:
      el += self.right.pre_order_traversal()

    return el

  def post_order_traversal(self):
    el = []
    if self.left:
      el += self.left.post_order_traversal()
    if self.right:
      el += self.right.post_order_traversal()
    el.append(self.data)
    return el


def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])
  for i in range(1, len(elements)):
    root.add_child(elements[i])
  return root


if __name__ == "__main__":
  countries = ["India", "Pakistan", "Germany",
               "USA", "China", "India", "UK", "USA"]
  country_tree = build_tree(countries)

  # print("UK is in the list? ", country_tree.search("UK"))
  # print("Sweden is in the list? ", country_tree.search("Sweden"))

  numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
  print("In order traversal gives this sorted list:",
        numbers_tree.in_order_traversal())
  print("Pre order traversal gives this sorted list:",
        numbers_tree.pre_order_traversal())
  print("Post order traversal gives this sorted list:",
        numbers_tree.post_order_traversal())
  print("Min:", numbers_tree.find_min())
  print("Max:", numbers_tree.find_max())
  print("Sum:", numbers_tree.calculate_sum())
