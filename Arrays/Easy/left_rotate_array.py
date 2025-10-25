# Left Rotate Array by k places
# @pattern-log : Simply store the values that gets displaced from left in a temp variable, shift
# the elements to the left by the displaced values, and place this temp at the right end of the array
# Time-Complexity : O(n) iterating through the nums
# Space-Complexity : O(k) Need to create a temp array of size k

def leftRotateArray(nums: list, k: int) -> None:
    n = len(nums)
    k = k % n  # left rotating a array by n places becomes same array, so we will be just shifting by number that matters

    temp = nums[:k]
    # storing the first k elements

    for i in range(k, n):
        nums[i-k] = nums[i]  # nums[0] = nums[3], nums[1] = nums[4]

    nums[n-k:] = temp


# [1, 4, 5, 7, 8, 2, 6, 8] , k= 3
# expected will be [1, 4, 5] will be added to the right of [7, 8, 2, 6, 8]
# expected is [7, 8, 2, 6, 8, 1, 4, 5]
nums = [1, 4, 5, 7, 8, 2, 6, 8]
k = 3
leftRotateArray(nums, k)
print(nums)
