from task_0 import Tree
import pytest


def test_min_value():
    try:
        trees = Tree(1)
        trees.list_insert([5, 7, 15])
        assert trees.min_value() == "1"
        print("test_min_value - passed")
    except:
        print("test_min_value - failed")


def test_max_value():
    try:
        trees = Tree(1)
        trees.list_insert([5, 7, 15])
        assert trees.max_value() == "15"
        print("test_max_value - passed")
    except:
        print("test_max_value - failed")


def test_list_insert():
    try:
        trees = Tree(12)
        trees.list_insert([1, 5, 7, 15])
        trees2 = Tree(1)
        assert trees.min_value() == trees2.min_value()
        print("test_list_insert - passed")
    except:
        print("test_list_insert - failed")


def test_delete():
    try:
        trees = Tree(12)
        trees.list_insert([5, 7, 15])
        trees.delete_node(15)
        trees2 = Tree(15)
        assert trees.max_value() != trees2.max_value()
        print("test_delete - passed")
    except:
        print("test_delete - failed")
