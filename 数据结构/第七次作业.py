# 定义二叉树节点
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 根据数组创建二叉树
def build_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None

    root = TreeNode(arr[index])
    root.left = build_tree(arr, 2 * index + 1)
    root.right = build_tree(arr, 2 * index + 2)
    
    return root


# 打印二叉树（横向）
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)

        print("    " * level + str(node.val))

        print_tree(node.left, level + 1)


# 给定数组
arr = [10, 5, 15, 3, 7, None, 20]

# 创建二叉树
root = build_tree(arr)

# 输出树结构
print("二叉树结构：")
print_tree(root)