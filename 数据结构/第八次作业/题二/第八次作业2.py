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
    if root is not None:
        print(prefix + ("├── " if is_left else "└── ") + str(root.key))
        if root.left or root.right:
            print_tree(root.left, prefix + ("│   " if is_left else "    "), True)
            print_tree(root.right, prefix + ("│   " if is_left else "    "), False)

def find_max(node):
    """找到以 node 为根的最大值节点（中序前驱用）"""
    while node.right:
        node = node.right
    return node

def find_min(node):
    """找到以 node 为根的最小值节点（中序后继用）"""
    while node.left:
        node = node.left
    return node

def delete_root_with_predecessor(root):
    """用左子树中的最大值（中序前驱）替换根节点，并删除原前驱"""
    if root is None:
        return None
    if root.left is None:
        # 没有左子树，直接返回右子树
        return root.right
    # 找前驱节点及其父节点
    parent = root
    pred = root.left
    while pred.right:
        parent = pred
        pred = pred.right
    # 用前驱的值覆盖根节点
    root.key = pred.key
    # 删除前驱节点
    if parent == root:
        parent.left = pred.left
    else:
        parent.right = pred.left
    return root

def delete_root_with_successor(root):
    """用右子树中的最小值（中序后继）替换根节点，并删除原后继"""
    if root is None:
        return None
    if root.right is None:
        return root.left
    parent = root
    succ = root.right
    while succ.left:
        parent = succ
        succ = succ.left
    root.key = succ.key
    if parent == root:
        parent.right = succ.right
    else:
        parent.left = succ.right
    return root

# 构建原 BST
values = [50, 30, 70, 20, 40, 60, 80]
root = None
for v in values:
    root = insert(root, v)

print("原始 BST：")
print_tree(root)
print("\n")

# 方法1：用中序前驱删除根节点
root1 = None
for v in values:
    root1 = insert(root1, v)
root1 = delete_root_with_predecessor(root1)
print("方法1：用中序前驱（左子树最大值）删除根节点 50 后的 BST：")
print_tree(root1)
print("\n")

# 方法2：用中序后继删除根节点
root2 = None
for v in values:
    root2 = insert(root2, v)
root2 = delete_root_with_successor(root2)
print("方法2：用中序后继（右子树最小值）删除根节点 50 后的 BST：")
print_tree(root2)

# 回答问题
print("\n")
print("注意问题：两种删除节点的方法能混用吗？")
print("答：不能混用。在单次删除操作中，只能选择其中一种策略（中序前驱或中序后继）来找到替代节点。")
print("混用会导致逻辑冲突，既替换成前驱又替换成后继，破坏二叉搜索树的结构和有序性。")
