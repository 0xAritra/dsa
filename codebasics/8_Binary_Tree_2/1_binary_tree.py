# deletion *
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
    sum = self.data
    if self.left:
      sum += self.left.calculate_sum()
    if self.right:
      sum += self.right.calculate_sum()
    return sum

  def find_min(self):
    if self.left:
      return self.left.find_min()
    return self.data

  def find_max(self):
    if self.right:
      return self.right.find_max()
    return self.data

  def delete(self, val):
    if val < self.data:
      if self.left:
        self.left = self.left.delete(val)

    elif val > self.data:
      if self.right:
        self.right = self.right.delete(val)

    else:
      if self.left is None and self.right is None:
        return None
      if self.left is None:
        return self.right
      if self.right is None:
        return self.left

      max_val = self.left.find_max()
      self.data = max_val
      self.left = self.left.delete(max_val)

    return self


def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])
  for i in range(1, len(elements)):
    root.add_child(elements[i])
  return root


if __name__ == "__main__":
  numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
  numbers_tree.delete(20)
  # this should print [1, 4, 9, 17, 18, 23, 34]
  print("After deleting 20 ", numbers_tree.in_order_traversal())

  numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
  numbers_tree.delete(9)
  # this should print [1, 4, 17, 18, 20, 23, 34]
  print("After deleting 9 ", numbers_tree.in_order_traversal())

  numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
  numbers_tree.delete(17)
  # this should print [1, 4, 9, 18, 20, 23, 34]
  print("After deleting 17 ", numbers_tree.in_order_traversal())
