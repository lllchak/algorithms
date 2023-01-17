from utils import dtypes


def check(func: dtypes.Callable, ground_truth: dtypes.Any, **kwargs) -> None:
    """
    Testing tasks function. Receives a function to check with its
    argumens and an expected answer. Simply print out your answer and expected one.

    Args:
        func (dtypes.Callable)    : Function to check
        ground_truth (dtypes.Any) : Expected answer
        **kwargs                  : Function to check parameters
    """

    print(f"Function result:\n\t{func(**kwargs)}")
    print(f"Expected answer\n\t{ground_truth}")
    