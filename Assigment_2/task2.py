def is_palindrome(s: str) -> bool:
    """Return True if string s is a palindrome, ignoring non-alphanumeric characters and case.

    Examples:
    is_palindrome("A man, a plan, a canal: Panama") -> True
    is_palindrome("racecar") -> True
    is_palindrome("hello") -> False
    """
    # Ensure we have a string
    text = str(s)
    # Keep only alphanumeric characters and lowercase them
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    # Check palindrome by comparing to its reverse
    return cleaned == cleaned[::-1]


# Small CLI example:
if __name__ == "__main__":
    user_input = input("Enter text to check for palindrome: ")
    result = is_palindrome(user_input)
    if result:
        print("Yes — it's a palindrome.")
    else:
        print("No — not a palindrome.")