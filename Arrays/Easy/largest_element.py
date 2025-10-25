# @pattern-log : Return the largest element by using max method over list, or store the max in a variable
# when traversing through the list and update the variable
# Space-Complexity : O(1) only one variable would be used
# Time-Complexity : O(n) iterating through the list once

def largestElement(nums: list) -> int:
    if len(nums):
        return max(nums)
    return -1
