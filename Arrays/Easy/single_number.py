# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# @pattern-log : a ^ a is 0. 0 ^ b is b. So if there are duplicates, those duplicates cancel each other and the single number will be revealed.
# Time-Complexity : O(n)
# Space-Complexity : O(1)

def singleNumber(self, nums: List[int]) -> int:
    missing = nums[0]
    for i in range(1, len(nums)):
        missing = missing ^ nums[i]

    return missing
