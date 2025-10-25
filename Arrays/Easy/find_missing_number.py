# Find missing number in a sequence array till N
# @pattern-log : Sum of sequence from 1 to N is N*(N+1)/2. If we subtract the nums from it, we shall
# get the missing number.
# missing_number + sum(nums) = Total Sequence sum till N = N(N+1)/2
# Time Complexity: O(n) - Sum of nums
# Space Complexity: O(1) - Only constant variables used
def findMissing(nums: list, N: int) -> int:
    total_sum = N*(N+1)/2
    return total_sum - sum(nums)
