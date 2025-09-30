# @pattern-log: Extract last digit with % 10, remove it with // 10, build reverse by multiplying by 10 and adding remainder
# Time Complexity: O(log n) - Number of iterations equals number of digits
# Space Complexity : O(1) - Space used does not grow with input size
def reverse_number(n: int) -> int:
    reverse_number = 0
    while n > 0:
        remainder = n % 10
        n = n // 10
        reverse_number = reverse_number*10 + remainder

    return reverse_number
