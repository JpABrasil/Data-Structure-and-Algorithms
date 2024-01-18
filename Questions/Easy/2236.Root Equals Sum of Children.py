def checkTree(self, root):
    if root.left.val + root.right.val == root.val:
        return True
    else:
        return False