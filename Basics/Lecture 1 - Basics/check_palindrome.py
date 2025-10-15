# @pattern-log: Reverse the number using digit extraction pattern, then compare with original
# Time Complexity: O(log n) - Number of iterations equals number of digits
def check_palindrome(n: int) -> bool:
    reverse = 0
    original = n
    while n > 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = n // 10

    return reverse == original
