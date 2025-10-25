# @pattern-log: Use two variables to track largest and second largest elements.
# For each element: if it's greater than largest, update both variables.
# If it's greater than second largest (but not equal to largest), update second largest.

# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(1) - Only two variables used regardless of input size

def secondLargest(nums: list) -> int:

    if len(nums) < 2:
        return -1  # Empty list and single list will be given -1

    largest = float('-inf')
    second_largest = float('-inf')

    for i in nums:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
            second_largest = i

    return second_largest
