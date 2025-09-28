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
