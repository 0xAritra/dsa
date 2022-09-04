from logging import root


class TreeNode:
  def __init__(self, name, role):
    self.data = {
      "name": name,
      "designation": role
    }
    self.parent = None
    self.children = []
  
  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  def get_levels(self):
    p = self.parent
    l = 0
    while p:
      l += 1
      p = p.parent
    return l

  def print_tree(self, item):
    if (item == "name" or item == "designation"):
      value = self.data[item]
    elif (item == "both"):
      value = self.data["name"] + " (" + self.data["designation"] + ")"
    space = self.get_levels() * " " * 3
    prefix = space + "|__" if self.parent else ""
    print(prefix + value)
    for child in self.children:
      child.print_tree(item)

def build_management_tree():
  root = TreeNode("Nilupul", "CEO")
  
  cto = TreeNode("Chinmay", "CTO")
  infra_head = TreeNode("Vishwas", "Infrastructure Head")
  cto.add_child(infra_head)
  infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
  infra_head.add_child(TreeNode("Abhijit", "App Manager"))
  cto.add_child(TreeNode("Aamir", "Application Head"))

  hr = TreeNode("Gels", "HR Head")
  hr.add_child(TreeNode("Peter", "Recruitment Manager"))
  hr.add_child(TreeNode("Waqas", "Policy Manager"))

  root.add_child(cto)
  root.add_child(hr)

  return root

if __name__ == "__main__":
  root_node = build_management_tree()
  root_node.print_tree("name")
  root_node.print_tree("designation")
  root_node.print_tree("both")