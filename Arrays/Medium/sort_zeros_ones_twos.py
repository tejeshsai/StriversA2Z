# @pattern-log : Store the number of zeros, ones, twos in one pass, slice the index in nums and set the values in place.
# Time Complexity : O(n) - 2 Passes
# Space Complexity : O(1)
def sortZerosOnesTwos(nums: list) -> None:
    zeros = 0
    ones = 0
    twos = 0
    for i in nums:
        if i == 0:
            zeros += 1
        elif i == 1:
            ones += 1
        else:
            twos += 1

    nums[0:zeros] = [0]*zeros
    nums[zeros:ones+zeros] = [1]*ones
    nums[ones+zeros:] = [2]*twos

# @pattern-log : Dutch National Flag Algorithm - 3-way partitioning algorithm.
# Initialization: Three pointers are used: low, mid, and high.
# low points to the beginning of the array (where 0s should be placed).
# mid points to the current element being examined.
# high points to the end of the array (where 2s should be placed).
# if mid element is zero, swaps with low pointer, both updates by 1
# if mid element is 1, increment by 1
# if mid element is 2, swaps with high pointer, high pointer shall decrease by 1.
# This algorithm is particularly useful in scenarios requiring efficient categorization or sorting of data into three distinct groups.
# Time-Complexity : O(n) - Single pass
# Space Complexity : O(1) - only three pointers used irrespective of input size.


def sortDutchNationalFlagAlg(nums: list) -> None:
    low = 0  # aims to put the next zero element
    mid = 0  # aims for 1
    high = len(nums) - 1  # Aims for position for element 2

    while mid <= high:
        if nums[mid] == 0:
            # Swap the low and mid elements, increment low and mid by 1
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # if mid position is 1, simply move the mid by 1
            mid += 1
        else:
            # if mid encounters 2, it needs to go to high position. Swap mid and high elements, decrease the high pointer by 1(next second element shall go there)
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1


nums = [2, 0, 2, 1, 1, 0]
sortZerosOnesTwos(nums)
print(nums)

nums = [2, 0, 2, 1, 1, 0]
sortDutchNationalFlagAlg(nums)
print(nums)
