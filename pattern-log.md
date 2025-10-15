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
