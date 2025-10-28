# @pattern-log : Maintain a running count of consecutive 1s. When encountering a 0,
#               update the maximum count seen so far and reset the running count to zero.
# Time-Complexity : O(n) - Single pass through the array
# Space-Complexity : O(1) - Only using two variables (maxOne and count) regardless of input size
def findMaxConsecutiveOnes(nums: list) -> int:
    maxOne = 0
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            maxOne = max(maxOne, count)
            count = 0

    return maxOne


nums = [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
print(findMaxConsecutiveOnes(nums))
