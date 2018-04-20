# AVL Tree Python Code

# Tree Node class
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

# AVL tree class
class AVLTree(object):
    
    def insert(self, root, key):

        # 1 - Insert
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # 2 - Udate the height of the root
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # 3 - Get the balance factor
        balance = self.getBalance(root)

        # 4 - Balance the tree if necessary
            # Case 1
        if balance > 1 and key < root.left.value:
            return self.rightRotate(root)
            # Case 2
        if balance < -1 and key > root.right.value:
            return self.leftRotate(root)
            # Case 3
        if balance > 1 and key > root.left.value:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
            # Case 4
        if balance < -1 and key < root.right.value:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root


    def delete(self, root, key):
 
        # 1 - Delete
        if not root:
            return root
 
        elif key < root.value:
            root.left = self.delete(root.left, key)
 
        elif key > root.value:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right,
                                      temp.value)
 
        # If the tree has only one node, simply return it
        if root is None:
            return root
 
        # 2 - Update the height of the root
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        # 3 - Get the balance factor
        balance = self.getBalance(root)
 
        # 4 - Balance the tree if necessary
            # Case 1
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
            # Case 2
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
            # Case 3
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
            # Case 4
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root

    # Rotate to the left function
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        # Perform rotation
        y.left = z
        z.right = T2
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right))
 
        # Return the new root
        return y

    # Rotate to the right function
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        # Perform rotation
        y.right = z
        z.left = T3
 
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        # Return the new root
        return y
    
    # Get the height of the root
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
    
    # Get the balance factor
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
    
    # In order printing
    def inOrder(self, root):
 
        if not root:
            return
 
        self.inOrder(root.left)
        print("{0} ".format(root.value), end="")
        self.inOrder(root.right)
    
avlTree = AVLTree()
root = None
nums = [20, 25, 40, 59, 74, 10, 16, 90, 41, -57, 2, 64, -3, 15]

print("TEST EXAMPLE")

# Sorted Numbers
print("Sorted array:")
arr = nums
arr.sort()
print(arr)
 
for num in nums:
    root = avlTree.insert(root, num)
 
# In Order
print("In Order after insertion:")
avlTree.inOrder(root)
print()
 
# Delete
key = 16
root = avlTree.delete(root, key)
 
# In Order after deletion
print("In Order after deletion:")
avlTree.inOrder(root)
print()

