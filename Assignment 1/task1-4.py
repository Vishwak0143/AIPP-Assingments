# ...existing code...
def factorial_iter(n: int) -> int:
    # Factorial will be calculated using iteration.
    if n < 0:
        raise ValueError("factorial undefined for negative integers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n: int) -> int:
    # Factorial will be calculated using recursion
    if n < 0:
        raise ValueError("factorial undefined for negative integers")
    return 1 if n <= 1 else n * factorial_rec(n - 1)

if __name__ == "__main__":
    # Ask the user for input and prints both iterative and recursive results.
    try:
        n = int(input("Enter a non-negative integer: ").strip())
        if n < 0:
            print("Error: input must be a non-negative integer")
        else:
            print(f"Iterative: {factorial_iter(n)}")
            print(f"Recursive: {factorial_rec(n)}")
    except ValueError:
        print("Invalid input")
# ...existing code...