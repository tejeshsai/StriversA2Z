# Algorithm Patterns Log

## Digit Manipulation Pattern

**Core Concept**: To count digits or process them one by one, repeatedly floor divide by 10 until the number becomes 0.

**When to use**: 
- Counting digits in a number
- Processing digits one by one (right to left)
- Reversing numbers
- Extracting individual digits
- Checking palindromes

**Pattern**:
```python
while n > 0:
    digit = n % 10    # Extract rightmost digit
    n = n // 10       # Remove rightmost digit
    # Process the digit
```

**Examples**:
- **Count digits**: `123 → 12 → 1 → 0` (3 iterations = 3 digits)
- **Reverse number**: Extract digits and build reverse
- **Sum of digits**: Add each extracted digit
- **Check palindrome**: Compare digits from both ends

**Key insight**: `// 10` removes the rightmost digit, `% 10` extracts it.

## Euclidean Algorithm Pattern

**Core Concept**: GCD(a,b) = GCD(b, a%b) - repeatedly replace larger number with remainder until one becomes 0.

**When to use**:
- Finding Greatest Common Divisor (GCD)
- Finding Highest Common Factor (HCF)
- Reducing fractions to simplest form
- Solving modular arithmetic problems

**Pattern**:
```python
while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a
return a if a > 0 else b
```

**Examples**:
- **GCD(48, 18)**: 48 % 18 = 12, then 18 % 12 = 6, then 12 % 6 = 0 → GCD = 6
- **GCD(17, 13)**: 17 % 13 = 4, then 13 % 4 = 1, then 4 % 1 = 0 → GCD = 1

**Key insight**: Each iteration reduces the problem size by at least half, making it O(log min(a,b)).

## Hash Map / Frequency Counting Pattern

**Core Concept**: Use a dictionary (hash map) to store counts or to map values to metadata (like first index) for O(1)-average inserts/updates/lookups.

**When to use**:
- Counting frequencies of numbers, characters, or tokens
- Tracking presence/occurrence seen-so-far
- Storing value → first_index/last_index for constant-time retrieval
- Detecting duplicates or building histograms
- Finding min/max frequency elements after counting

**Pattern**:
```python
from collections import defaultdict

def count_frequency(items):
    freq = defaultdict(int)
    for x in items:
        freq[x] += 1
    return freq  # dict-like: iterate or query as needed
```

Alternative without `defaultdict`:
```python
def count_frequency(items):
    freq = {}
    for x in items:
        freq[x] = freq.get(x, 0) + 1
    return freq
```

Value → index mapping (e.g., for two-sum-like lookups):
```python
def build_index_map(items):
    index_of = {}
    for i, x in enumerate(items):
        if x not in index_of:
            index_of[x] = i  # store first occurrence (or update for last)
    return index_of
```

**Complexity**:
- Time: O(n) to build over n items
- Space: O(k) where k is the number of unique keys

**Key insight**: Default-initialize counts with `defaultdict(int)` to avoid conditionals; use `.get()` when not relying on `defaultdict`.

```python
# After building freq, scan once to get min/max frequency elements
min_elem = min(freq, key=freq.get)
max_elem = max(freq, key=freq.get)
```

## Two Pointer Pattern

**Core Concept**: Use two pointers to traverse an array from different positions, typically one slow and one fast, to solve problems in-place with O(1) space.

**When to use**:
- Removing duplicates from sorted arrays
- Finding pairs that sum to a target
- Merging two sorted arrays
- Detecting cycles in linked lists
- Partitioning arrays based on conditions
- Finding subarrays with specific properties

**Pattern**:
```python
def two_pointer_approach(nums):
    left = 0  # Slow pointer - tracks position for next valid element
    right = 1  # Fast pointer - scans ahead to find next different element
    
    while right < len(nums):
        if nums[left] == nums[right]:
            right += 1  # Skip duplicates
        else:
            nums[left + 1] = nums[right]  # Place unique element
            left += 1
            right += 1
    
    return left + 1  # New length
```

**Key variations**:
- **Opposite ends**: Start from both ends and move inward
- **Same direction**: Both pointers move in same direction at different speeds
- **Fast-slow**: One pointer moves twice as fast as the other

**Examples**:
- **Remove duplicates**: `[1,1,2,2,3] → [1,2,3]`
- **Move zeros to end**: `[1,0,2,3,0,4] → [1,2,3,4,0,0]`
- **Two sum**: Find pair that sums to target
- **Palindrome check**: Compare characters from both ends

**Key insight**: One pointer tracks the "write position" while the other scans for "valid elements" to write.

## Mathematical Patterns

### Arithmetic Sequence Sum Pattern

**Core Concept**: Use mathematical formulas to solve problems involving sequences, especially finding missing elements or calculating sums efficiently.

**When to use**:
- Finding missing numbers in sequences
- Calculating sums of arithmetic progressions
- Validating sequence completeness
- Finding duplicates using mathematical properties
- Optimizing sum calculations

**Pattern**:
```python
def find_missing_in_sequence(nums, n):
    # Sum of arithmetic sequence 1 to n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

**Mathematical Formula**:
- **Sum of 1 to n**: `n * (n + 1) / 2`
- **Sum of a to b**: `(b - a + 1) * (a + b) / 2`
- **Missing number**: `Expected Sum - Actual Sum`

**Examples**:
- **Find missing number**: `[1,2,4,5]` with n=5 → Missing = 3
- **Validate sequence**: Check if array contains all numbers 1 to n
- **Find duplicate**: If sum exceeds expected, find the duplicate

**Key insight**: Mathematical formulas can often replace complex algorithms, providing O(1) space solutions for sequence problems.

## Bit Manipulation Patterns

### XOR Properties Pattern

**Core Concept**: XOR has unique properties that make it perfect for finding single elements in arrays with duplicates, detecting differences, and toggling bits.

**Key XOR Properties**:
- `a ^ a = 0` (any number XORed with itself equals 0)
- `a ^ 0 = a` (any number XORed with 0 equals itself)
- `a ^ b = b ^ a` (commutative property)
- `(a ^ b) ^ c = a ^ (b ^ c)` (associative property)

**When to use**:
- Finding single element in array where all others appear twice
- Detecting differences between two arrays
- Toggling bits (XOR with 1 flips the bit)
- Finding missing numbers using XOR properties
- Swapping two numbers without temporary variable

**Pattern**:
```python
def find_single_element(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR all elements
    return result
```

**Examples**:
- **Single Number**: `[2,1,2,1,3]` → All pairs cancel out, only 3 remains
- **Missing Number**: XOR expected sequence with actual array
- **Swap without temp**: `a ^= b; b ^= a; a ^= b`
- **Toggle bits**: `num ^= (1 << position)` flips bit at position

**Complexity**:
- Time: O(n) - single pass through array
- Space: O(1) - only one variable needed

**Key insight**: XOR's self-canceling property (`a ^ a = 0`) makes it perfect for eliminating duplicates and finding unique elements efficiently.

### Prefix Sum + Hashmap Pattern

**Core Concept**: Use prefix sums to efficiently find subarrays with specific properties by storing prefix sum information in a hashmap for O(1) lookups.

**When to use**:
- Finding subarrays with specific sum (works with negative numbers)
- Counting subarrays that sum to a target
- Finding longest/shortest subarrays with given sum
- Problems involving contiguous subarray sums
- When sliding window fails due to negative numbers

**Pattern**:
```python
def subarray_with_sum(nums, k):
    prefix_map = {0: -1}  # Handle subarrays starting from index 0
    prefix_sum = 0
    result = 0  # max length, count, etc.
    
    for i, num in enumerate(nums):
        prefix_sum += num
        target = prefix_sum - k
        
        if target in prefix_map:
            # Found a subarray that sums to k
            # Calculate length: i - prefix_map[target]
            # Or increment count: result += prefix_map[target]
            result = max(result, i - prefix_map[target])
        
        # Store prefix sum (for length: only first occurrence, for count: all occurrences)
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i
        # For counting: prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return result
```

**Key insight**: `subarray_sum(i,j) = prefix_sum[j] - prefix_sum[i-1]`. If we want sum = k, we need `prefix_sum[j] - prefix_sum[i-1] = k`, which means `prefix_sum[i-1] = prefix_sum[j] - k`.

**Examples**:
- **Longest subarray with sum k**: Store first occurrence of each prefix sum
- **Count subarrays with sum k**: Store count of occurrences of each prefix sum
- **Subarray sum equals k**: Works with both positive and negative numbers

**Complexity**:
- Time: O(n) - single pass through array
- Space: O(n) - hashmap stores at most n prefix sums

**Key insight**: The prefix sum technique transforms subarray problems into lookup problems, making them solvable in O(n) time even with negative numbers.
