def is_palindrome(text):
  """
  Checks if a given string is a palindrome (reads the same forwards and backwards).

  Args:
    text: The string to check.

  Returns:
    True if the string is a palindrome, False otherwise.
  """
  # Remove spaces and convert to lowercase for case-insensitive check
  cleaned_text = text.replace(" ", "").lower()
  return cleaned_text == cleaned_text[::-1]

# Example usage with input and output:
user_input = input("Enter a string to check if it's a palindrome: ")

if is_palindrome(user_input):
  print(f"'{user_input}' is a palindrome.")
else:
  print(f"'{user_input}' is not a palindrome.")