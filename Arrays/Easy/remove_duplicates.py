# Remove Duplicates In Place
# @pattern-log: Two pointer approach - left pointer points to position where next unique element should be placed,
# right pointer scans ahead to find the next different element, then places it at the successor position.
# Time Complexity: O(n) - Both pointers traverse the array once
# Space Complexity: O(1) - Only two variables used

def removeDuplicates(nums: list) -> int:
    i = 0
    j = 1

    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            nums[i+1] = nums[j]
            i += 1

    return i+1


nums = [1, 1, 3, 5, 5, 5, 6]
removeDuplicates(nums)
print(nums)
