import sys

def largest_in_list(nums):
    # Return the largest item from a list of numbers.
    # Raise ValueError for an empty list so callers know it's invalid.
    if not nums:
        raise ValueError("largest_in_list requires a non-empty list")
    return max(nums)

if __name__ == "__main__":
    # Prompt the user to enter numbers separated by spaces or commas.
    s = input("Enter numbers (separated by spaces or commas): ").strip()
    if not s:
        print("No input provided")
        sys.exit(1)

    try:
        # Normalize commas to spaces, split, and convert tokens to numbers.
        parts = s.replace(',', ' ').split()
        numbers = [float(p) if ('.' in p or 'e' in p.lower()) else int(p) for p in parts]

        # Print the largest number found.
        print(f"Largest number: {largest_in_list(numbers)}")
    except ValueError:
        # Handle cases where conversion to a number fails.
        print("Invalid input: please enter valid numbers")
# filepath: d:\VS Code\AIPP\Assignments\task1-5.py
import sys

def largest_in_list(nums):
    # Return the largest item from a list of numbers.
    # Raise ValueError for an empty list so callers know it's invalid.
    if not nums:
        raise ValueError("largest_in_list requires a non-empty list")
    return max(nums)

if __name__ == "__main__":
    # Prompt the user to enter numbers separated by spaces or commas.
    s = input("Enter numbers (separated by spaces or commas): ").strip()
    if not s:
        print("No input provided")
        sys.exit(1)

    try:
        # Normalize commas to spaces, split, and convert tokens to numbers.
        parts = s.replace(',', ' ').split()
        numbers = [float(p) if ('.' in p or 'e' in p.lower()) else int(p) for p in parts]

        # Print the largest number found.
        print(f"Largest number: {largest_in_list(numbers)}")
    except ValueError:
        # Handle cases where conversion to a number fails.
        print("Invalid input: please enter valid numbers")