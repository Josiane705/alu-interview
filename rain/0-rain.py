#!/usr/bin/python3
"""
0-rain
Calculates the total amount of rainwater retained
given a list of wall heights.
"""


def rain(walls):
    """
    Calculate the amount of water retained after it rains.

    Args:
        walls (list): List of non-negative integers representing wall heights.

    Returns:
        int: Total amount of water retained.
    """
    if not walls or len(walls) < 3:
        return 0

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                total_water += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                total_water += right_max - walls[right]
            right -= 1

    return total_water
