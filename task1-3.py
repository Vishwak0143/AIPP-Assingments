def reverse_string(s: str) -> str:
    """
    Return the reverse of the input string.
    Raises 'TypeError' if s is not a string.
    """
    if not isinstance(s, str):
        raise TypeError("reverse_string expects a str")
    return s[::-1]

# ...existing code...
if __name__ == "__main__":
    s = input("Enter a string: ")
    print(reverse_string(s))
# ...existing code...