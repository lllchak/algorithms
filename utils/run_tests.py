from utils import dtypes


def check_print(func: dtypes.Callable, ground_truth: dtypes.Any, **kwargs) -> None:
    """
    Testing tasks function. Receives a function to check with its
    argumens and an expected answer. Since answers can be in any order 
    simply print out your answer and expected one.

    Args:
        func (dtypes.Callable)    : Function to check
        ground_truth (dtypes.Any) : Expected answer
        **kwargs                  : Function to check parameters
    """

    print(f"Function result:\n\t{func(**kwargs)}")
    print(f"Expected answer\n\t{ground_truth}")


def check_eq(func: dtypes.Callable, ground_truth: dtypes.Any, **kwargs) -> bool:
    """
    Testing tasks function. Receives a function to check with its
    argumens and an expected answer. Returns bool flag if func output
    mathes the expected one

    Args:
        func (dtypes.Callable)    : Function to check
        ground_truth (dtypes.Any) : Expected answer
        **kwargs                  : Function to check parameters
    """
    
    return ground_truth == func(**kwargs)
    