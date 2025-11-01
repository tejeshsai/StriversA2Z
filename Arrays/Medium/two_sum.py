# @pattern-log : Storing the elements of nums in hashmap (value -> index) while iterating as well as checking if there is an element we passed through that we get k by adding the current element.
# Time Complexity : O(n)
# Space Complexity : O(n)

def twoSum(nums: list, k: int) -> list:
    hashmap = {}
    for i, num in enumerate(nums):
        target = k - num
        if target in hashmap:
            return [hashmap[target], i]
        else:
            hashmap[num] = i
    return [-1, -1]


print(twoSum([2, 5, 3, 7, 8], 7))
