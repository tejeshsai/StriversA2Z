# Problem statement: Given an array, we have found the number of occurrences of each element in the array.
# @pattern-log : If you want to count frequencies for numbers or alphabets in a list, or store value : index
# to be retireved in constant time, use dictionary (hashmap)
# Time-Complexity : O(n)
# Space-Complexity : O(n) in the worst case (n unique elements); generally O(k) for k uniques
from collections import defaultdict


def countFrequency(nums: list) -> None:
    hashmap = defaultdict(int)
    for i in nums:
        hashmap[i] += 1

    for key, value in hashmap.items():
        print(key, value)


countFrequency([1, 5, 2, 1, 7, 2, 5])
