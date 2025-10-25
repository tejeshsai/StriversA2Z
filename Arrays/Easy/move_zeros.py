# Move Zeros to the end in place
# @pattern-log: Two pointer approach - i only moves when the ith position is filled with a non-zero element,
# j moves until it finds a non-zero element to swap with the zero at position i.
# Time Complexity: O(n) - Both pointers traverse the array once
# Space Complexity: O(1) - Only two variables used

def moveZeros(nums: list) -> None:
    i = 0
    j = 1

    while j < len(nums) and i < len(nums):
        if nums[i] != 0:
            i += 1
        else:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            j += 1


nums = [1, 0, 2, 3, 0, 4, 0, 1]

moveZeros(nums)
print(nums)
