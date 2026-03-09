"""Practice with lists!"""

__author__ = "730748019"


def all(input: list[int], num: int) -> bool:
    """Return True if all values in input equal num."""

    if len(input) == 0:
        return False

    for value in input:
        if value != num:
            return False

    return True


def max(input: list[int]) -> int:
    """Return the largest value in the list. Raises ValueError if the list is empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest: int = input[0]

    for value in input:
        if value > largest:
            largest = value
    # For function loops through the list comparing each input to the next until it finds the largest value
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """First compares the lengths of the lists, returns false if they are different"""
    if len(list1) != len(list2):
        return False

    index: int = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1
    # Goes through each index of both of the lists and compares them, returns true if all of them are equal
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Defines the extend function that will add list2 to list1"""
    for value in list2:
        list1.append(value)
