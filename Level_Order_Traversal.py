class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


    def level_order(self,root):
        if root is None:
            return
        queue = []
        queue.append(root)
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print(result)
    
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    a = Node(root)
    a.level_order(root)
main()
