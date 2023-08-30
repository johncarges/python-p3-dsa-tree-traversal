class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_check = [self.root]
    while len(nodes_to_check) > 0 :
      node = nodes_to_check.pop(0)
      if node["id"] == id:
        return node
      else:
        nodes_to_check += node["children"]
    return None





