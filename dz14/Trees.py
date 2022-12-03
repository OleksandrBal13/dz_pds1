class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    def insert_list(self, list):
        for id_node in list:
            self.insert(id_node)

    def min_value(self):
        while self.left is not None:
            self = self.left
        return str(self)

    def max_value(self):
        while self.right is not None:
            self = self.right
        return str(self)

    def delete_node(node, key):
        if node is None:
            return node
        if key < node.id_node:
            node.left = node.left.delete_node(key)
        elif key > node.id_node:
            node.right = node.right.delete_node(key)
        else:
            if node.left is None:
                temp = node.right
                return temp
            elif node.right is None:
                temp = node.left
                return temp
            temp = node.right.minValueNode()
            node.id_node = temp.id_node
            node.right = node.right.deleteNode(temp.id_node)
        return node