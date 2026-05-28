# -*- coding: utf-8 -*-
"""
Created on Thu May 28 23:26:16 2026

@author: Administrator
"""

############题一##################
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def print_tree(root, prefix="", is_left=True):
    """递归打印树的结构，便于观察"""
    if root is not None:
        print(prefix + ("├── " if is_left else "└── ") + str(root.key))
        # 递归打印左子树和右子树，调整前缀
        if root.left or root.right:
            print_tree(root.left, prefix + ("│   " if is_left else "    "), True)
            print_tree(root.right, prefix + ("│   " if is_left else "    "), False)

# 构建BST
values = [50, 30, 70, 20, 40, 60, 80]
root = None
for v in values:
    root = insert(root, v)

print("最终BST：")
print_tree(root)