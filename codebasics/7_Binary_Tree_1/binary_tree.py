class BinarySearchTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    if data == self.data:
      return

    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinarySearchTreeNode(data)

    else:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinarySearchTreeNode(data)

  def search(self, val):
    if val == self.data:
      return True

    elif val < self.data:
      if self.left:
        return self.left.search(val)
      else:
        return False

    else:
      if val > self.data:
        if self.right:
          return self.right.search(val)
        else:
          return False

  def in_order_traversal(self):
    elements = []
    if self.left:
      elements += self.left.in_order_traversal()

    elements.append(self.data)

    if self.right:
      elements += self.right.in_order_traversal()

    return elements


def build_tree(values):
  root = BinarySearchTreeNode(values[0])
  for i in range(1, len(values)):
    root.add_child(values[i])
  return root


if __name__ == "__main__":
  countries = ["India", "Pakistan", "Germany",
               "USA", "China", "India", "UK", "USA"]
  country_tree = build_tree(countries)

  print("country tree, in order traversal:", country_tree.in_order_traversal())

  print("UK is in the list? ", country_tree.search("UK"))
  print("Sweden is in the list? ", country_tree.search("Sweden"))

  numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
  print("In order traversal gives this sorted list:",
        numbers_tree.in_order_traversal())
