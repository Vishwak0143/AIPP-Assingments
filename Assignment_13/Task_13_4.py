"""Small refactor: compute squares more concisely and efficiently."""

def compute_squares(nums):
    """Return a list of squares for numbers in `nums`.

    Uses a list comprehension which is more concise and faster than
    appending in a loop for this simple case.
    """
    return [x * x for x in nums]


if __name__ == '__main__':
    nums = list(range(1, 11))
    squares = compute_squares(nums)
    print('Nums   :', nums)
    print('Squares:', squares)
