class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


    def height_of_tree(self, root):
        if root is None:
            return 0
        queue = []
        queue.append(root)
        height = 0
        while True:
            node_count = len(queue)
            if node_count == 0:
                print("The height of the tree is ", height)
                return height
            height += 1

            while node_count:
                node = queue[0]
                queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                node_count -= 1

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    a = Node(root)
    a.height_of_tree(root)

main()
