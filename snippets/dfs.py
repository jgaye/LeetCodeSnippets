from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    return dfs_max_depth(0, root)


def dfs_max_depth(acc: int, node: Optional[TreeNode]) -> int:
    """
    Recursively return the maximum depth of a Tree
    By passing an incrementing value
    """
    if not node:
        return acc
    return max(dfs_max_depth(acc + 1, node.left), dfs_max_depth(acc + 1, node.right))


def dfs_acc_leaves(acc: List[int], node: Optional[TreeNode]) -> Optional[List[int]]:
    """
    Return the list of leaves values of a Tree
    """
    if not node:
        return

    if not node.left and not node.right:
        print(f"Found leaf {node.val}")
        acc.append(node.val)
        if len(acc) == 1:  # Case only 1 root node, we need to return the accumulator
            return acc
        return

    dfs_acc_leaves(acc, node.left)
    dfs_acc_leaves(acc, node.right)
    return acc


def build_tree(list_nodes: List[int]) -> TreeNode:
    root_node = TreeNode(val=list_nodes[0])
    nodes = [root_node]
    for i, x in enumerate(list_nodes[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = i % 2 == 0
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


def example():
    input = [3, 9, 20, None, None, 15, 7]
    root = build_tree(input)
    print(max_depth(root))


if __name__ == "__main__":
    example()
