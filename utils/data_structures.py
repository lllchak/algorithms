import dtypes


class ListNode:
    """
    Linked list node class. Stores node value with the pointer
    to the next node.

    Usage example:
        my_list = ListNode(1, ListNode(5, ListNode(3, None)))
        my_list = 1 -> 5 -> 3 -> NULL
    """

    def __init__(
        self,
        val: dtypes.Any = None,
        next: dtypes.Optional["ListNode"] = None
    ) -> None:
        self.val = val
        self.next = next


class TreeNode:
    """
    Binary tree node class. Stores node value with the pointers
    to the left and right subtrees.

    Usage example:
        my_tree = TreeNode(
            1, TreeNode(
                3, TreeNode(
                    2, None
                ), TreeNode(
                    6, None
                )
            ), TreeNode(
                4, None
            ), TreeNode(
                7, None
            )
        )
    """
    def __init__(
        self, 
        val: dtypes.Any = None,
        right: dtypes.Optional["TreeNode"] = None,
        left: dtypes.Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.right = right
        self.left = left


class N_aryTreeNode:
    """
    N-ary Binary tree node class. Stores node value and its children
    as a list of nodes.

    Usage example:
        my_tree = N_aryTreeNode(
            1, [N_aryTreeNode(3, None), N_aryTreeNode(6, None), N_aryTreeNode(1, None)]
        )
    """

    def __init__(
        self, 
        val: dtypes.Any = None,
        children: dtypes.List[dtypes.Any]=None
    ) -> None:
        self.val = val
        self.children = children
