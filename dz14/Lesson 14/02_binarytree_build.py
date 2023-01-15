# Creating binary tree
# from given list
from binarytree import *


# List of nodes
nodes =[8, 3, 10, 1, 6, None, 14, None, None, 4, 7, None, None, 13, None]
# Building the binary tree
binary_tree = build(nodes)
print('Binary tree from list :\n',
	binary_tree)

# Getting list of nodes from
# binarytree
print('\nList from binary tree :',
	binary_tree.values)

print('\nProperties:', binary_tree.properties)
