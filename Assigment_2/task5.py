# get numbers from user
user_input = input("Enter numbers separated by spaces: ")
numbers = []

# convert input to list of numbers
for num in user_input.split():
    try:
        numbers.append(int(num))
    except:
        pass

print(f"\nYour list: {numbers}")

# calculate sum of odd and even
odd_sum = 0
even_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of odd numbers: {odd_sum}")
print(f"Sum of even numbers: {even_sum}")

