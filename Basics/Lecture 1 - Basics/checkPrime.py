import math


def checkPrime(n: int) -> list[int]:
    square = int(math.sqrt(n))
    cnt = 0
    for i in range(1, square + 1):
        if n % i == 0:
            cnt = cnt + 1
            if n % i != i:
                cnt = cnt + 1
    
    return cnt == 2


print(checkPrime(3))
