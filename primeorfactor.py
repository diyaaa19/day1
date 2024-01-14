import math
n=int(input("Enter your number :"))


def factors(n):
    factor=[]
    for i in range(1,n+1):
        if n%i==0:
            factor.append(i)
    return factor


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print(n, "is a prime number.")
else:
    f=factors(n)
    print(f)
