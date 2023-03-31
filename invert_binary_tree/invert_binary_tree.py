
def invert_binary_tree(root):
    """
    Invert binary tree
    """
    # solve this recursive

    # base case
    if not root:
        return

    tmp = root.left
    root.left = root.right
    root.right = tmp

    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
