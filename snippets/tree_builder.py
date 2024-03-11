from __future__ import annotations

from typing import Optional, List

from snippets.dfs import max_depth


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"""TreeNode val:{self.val} left:{"node" if self.left else "None"} right:{"node" if self.right else "None"}"""


def tree_builder(array_nodes: List[int]) -> Optional[TreeNode]:
    """
    Build a tree based on the passed array (list of values)
    In the form of a heap (https://docs.python.org/3/library/heapq.html#theory)
    And returns the Root

    For example, [1,2,3,None,5,None,4] will give
            1
           / \
          2   3
           \   \
            5   4
    """
    if not array_nodes:
        return None

    root = TreeNode(
        val=array_nodes[0],
        left=build_node(1, array_nodes),
        right=build_node(2, array_nodes),
    )
    return root


def build_node(index: int, array_nodes: List[int]) -> Optional[TreeNode]:
    try:
        if not array_nodes[index]:
            curr = None
        else:
            curr = TreeNode(
                val=array_nodes[index],
                left=build_node(2 * index + 1, array_nodes),
                right=build_node(2 * index + 2, array_nodes),
            )
    except IndexError:
        curr = None
    return curr


def tree_printer(root: Optional[TreeNode]) -> str:
    depth = max_depth(root)
    width = pow(2, depth - 1)

    acc = f"""\n{root.val}\n"""
    acc += print_tree_row([root.left, root.right], curr_depth=2, width=width)
    print(acc)

    return acc


def print_tree_row(nodes: List[Optional[TreeNode]], curr_depth: int, width: int) -> str:
    acc = ""
    children = []
    for node in nodes:
        suffix = "\t" * (width // pow(2, curr_depth - 1))
        if not node:
            acc += f"Ø{suffix}"
            children.append(None)
            children.append(None)
        else:
            acc += f"{str(node.val)}{suffix}"
            children.append(node.left)
            children.append(node.right)

    acc.rstrip("\t")
    if [c for c in children if c]:
        acc += f"\n{print_tree_row(children, curr_depth=curr_depth+1, width=width)}"

    return acc
