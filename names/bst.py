class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
      if value < self.value:
        if self.left is None:
           self.left = BSTNode(value)
        else:
            self.left.insert(value)

      elif value >= self.value:
        if self.right is None:
           self.right = BSTNode(value)
        else:
            self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        highest = node.value
        while node != None:
            highest = node.value
            node = node.right
        return highest
