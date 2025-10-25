# Check if the array is sorted in ascending order
# @pattern-log: Compare each element with its previous element.
# If any element is smaller than its predecessor, the array is not sorted.
# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(1) - Constant space usage

def checkArraySorted(nums: list) -> bool:
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False

    return True
