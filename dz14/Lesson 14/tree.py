from Trees import Tree

# preorder traversal
list = []
def pre_order(node):
    if node:
        list.append(node.id_node)
        print(node.id_node)
        pre_order(node.left)
        pre_order(node.right)


# postorder traversal
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.id_node)

# inorder traversal
def in_order(node):
    if node:
        in_order(node.left)
        print(node.id_node)
        in_order(node.right)

tree = Tree(10)


tree.insert(7)
tree.insert(12)
tree.insert(8)
tree.insert(22)
tree.insert(14)

list = [1, 2, 3, 4, 5, 77, 43, 65]
tree.insert_list(list)
tree.print_tree()


