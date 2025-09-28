# @pattern-log : If you want to count the number of digits, or process digit by digit, floor divide it by 10
# Time Complexity: O(log n) - Number of iterations equals number of digits (log₁₀(n))

def countDigits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n = n // 10

    return count
