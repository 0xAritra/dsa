class TreeNode:
  def __init__(self, data):
    self.data = data
    self.parent = None
    self.children = []

  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def get_levels(self):
    l = 0
    p = self.parent
    while p:
      l += 1
      p = p.parent
    return l

  def print_tree(self, lvl):
    l = self.get_levels()
    spaces = " " * l * 3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix + self.data)
    for child in self.children:
      if (l < lvl):
        child.print_tree(lvl)


def build_location_tree():
  root = TreeNode("Global")

  ind = TreeNode("India")
  gj = TreeNode("Gujarat")
  gj.add_child(TreeNode("Ahmedabad"))
  gj.add_child(TreeNode("Baroda"))
  ka = TreeNode("Karnataka")
  ka.add_child(TreeNode("Bangalore"))
  ka.add_child(TreeNode("Mysuru"))

  usa = TreeNode("USA")
  nj = TreeNode("New Jersey")
  nj.add_child(TreeNode("Princeton"))
  nj.add_child(TreeNode("Trenton"))
  ca = TreeNode("California")
  ca.add_child(TreeNode("San Francsico"))
  ca.add_child(TreeNode("Mountain View"))
  ca.add_child(TreeNode("Palo Alto"))

  ind.add_child(gj)
  ind.add_child(ka)

  usa.add_child(nj)
  usa.add_child(ca)

  root.add_child(ind)
  root.add_child(usa)

  return root


if __name__ == "__main__":
  root_node = build_location_tree()
  root_node.print_tree(2)
