def maximum_of_three(first: float, second: float, third: float) -> float:
    """Return the largest of three numbers."""
    return max(first, second, third)


def maximum_of_four(
    first: float, second: float, third: float, fourth: float
) -> float:
    """Return the largest of four numbers."""
    return max(first, second, third, fourth)


print("Maximum of 10, 25, and 15:", maximum_of_three(10, 25, 15))
print("Maximum of 10, 25, 15, and 30:", maximum_of_four(10, 25, 15, 30))
