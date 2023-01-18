import dtypes


class ListNode:
    def __init__(
        self,
        val: dtypes.Any = None,
        next: dtypes.Optional["ListNode"] = None
    ) -> None:
        self.val = val
        self.next = next


class TreeNode:
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
    def __init__(
        self, 
        val: dtypes.Any = None,
        children: dtypes.List[dtypes.Any]=None
    ) -> None:
        self.val = val
        self.children = children
