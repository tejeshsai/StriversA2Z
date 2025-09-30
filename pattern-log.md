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
