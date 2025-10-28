# @pattern-log : store the prefix sums in a hashmap, if the sum till those elements - k exists,
# then the length of the subarray can the the index till this sub of elements - the index at which we find the prefix when added comes to k
# Time Complexity : O(n)
# Space Complexity : O(n)

def longestSubarray(nums: list, k) -> int:
    prefix_sum_index = {0: -1}
    maxLen = 0
    prefixSum = 0

    for i, x in enumerate(nums):
        prefixSum += x

        target = prefixSum - k
        if target in prefix_sum_index:
            maxLen = max(maxLen, i - prefix_sum_index[target])
        if not prefixSum in prefix_sum_index:
            prefix_sum_index[prefixSum] = i

    return maxLen


print(longestSubarray([2, 3, 5, 1, 1, 1, 1, 1], 10))
