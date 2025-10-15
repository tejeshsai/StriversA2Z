# Problem statement: Return the elements with the lowest and highest frequencies in the array.
# @pattern-log: Use a hash map to count frequencies, then scan the (key, count) pairs
#               while maintaining running min/max counters to find min/max-frequency elements.
# Time-Complexity: O(n) — one pass to count, one pass over unique keys
# Space-Complexity: O(k) where k is the number of unique elements (worst-case O(n))
from collections import defaultdict


def highLowFrequency(nums: list) -> list:
    if not nums:
        return []

    frequency_by_number = defaultdict(int)
    for value in nums:
        frequency_by_number[value] += 1

    min_count = float("inf")
    min_element = None
    max_count = 0
    max_element = None

    for number, count in frequency_by_number.items():
        if count < min_count:
            min_element = number
            min_count = count
        if count > max_count:
            max_element = number
            max_count = count

    return [min_element, max_element]


print(highLowFrequency([10, 5, 10, 15, 10, 5]))
