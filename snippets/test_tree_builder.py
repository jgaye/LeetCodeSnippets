from snippets.dfs import build_tree
from snippets.tree_builder import tree_builder, tree_printer


def test_small_tree():
    inp = [1, 2, 3, None, 5, None, 4]
    root = build_tree(inp)

    assert root.val == 1

    two = root.left
    assert two.val == 2
    assert two.left is None
    assert two.right.val == 5

    three = root.right
    assert three.val == 3
    assert three.left is None
    assert three.right.val == 4


def test_build_and_print():
    inp = [1, 2, 3, 4, None, None, 5, None, None, None, None, None, None, 6, 7]

    tree = tree_builder(inp)
    assert tree.left.left.val == 4
    assert tree.left.right is None
    assert tree.right.right.left.val == 6
    assert tree.right.right.right.val == 7

    expected_print = (
        "\n1\n2\t\t\t\t3\t\t\t\t\n4\t\tØ\t\tØ\t\t5\t\t\nØ\tØ\tØ\tØ\tØ\tØ\t6\t7\t"
    )
    assert tree_printer(tree) == expected_print
