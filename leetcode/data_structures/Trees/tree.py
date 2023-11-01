class Node:
    def __init__(self, data = None) -> None:
        
        self.data = data
        self.left_node = None
        self.right_node = None
        
    def search(self, data):
        
        if self.data == data:
            print("Found it")
            return self
        
        if self.right_node and self.data < data:
            return self.right_node.search(data)
        
        if self.left_node and self.data > data:
            return self.left_node.search(data)
        
        print("Target not in the tree")
        

class Tree:
    def __init__(self, root = None, name=""):
        self.root = root
        self.name = name

node = Node(10)

node.left_node = Node(7)
node.right_node = Node(20)
node.left_node.left_node = Node(5)
node.right_node.right_node = Node(50)

my_tree = Tree(node, "Emmanuel's Tree")

print(my_tree.root.data)
print(my_tree.root.left_node.data)

result = my_tree.root.search(50)

print(result.data)