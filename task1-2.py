def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

try:
    n = int(input("Enter integer: ").strip())
    print(f"{n} is a prime number" if is_prime(n) else f"{n} is not a prime number")
except ValueError:
    print("Invalid input")
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

try:
    n = int(input("Enter integer: ").strip())
    print(f"{n} is a prime number" if is_prime(n) else f"{n} is not a prime number")
except ValueError:
    print("Invalid input")