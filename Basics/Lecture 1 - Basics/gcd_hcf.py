# @pattern-log: Euclidean algorithm - repeatedly replace larger number with remainder of division until one becomes 0
# Time Complexity: O(log min(a,b)) - Each iteration reduces the problem size significantly
# Space Complexity: O(1) - Only using constant extra space
def gcd(n1: int, n2: int) -> int:
    while n1 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    if n1 == 0:
        return n2
    return n1
