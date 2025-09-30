# @pattern-log : Extract digits by floor dividing 10, add it by powering it by 3 to result
# Time Complexity : O(log n)
def checkArmstrong(n: int) -> bool:
    original = n
    result = 0
    while n > 0:
        digit = n % 10
        result = result + digit**3
        n = n // 10

    return original == result
