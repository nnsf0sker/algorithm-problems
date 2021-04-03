from typing import Any


def check_is_natural(value: Any, is_zero_natural: bool = False) -> None:
    """
    Raising error if value is natural
    """
    if not isinstance(value, int):
        raise TypeError(f"{type(value).__name__} is not instance of class {int.__name__}")
    if value < 0 or (value == 0 and not is_zero_natural):
        raise ValueError(f"{value} is not natural (less than {'or equal to ' * (not is_zero_natural)}0)")
