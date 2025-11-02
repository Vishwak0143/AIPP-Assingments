def sum_of_squares(numbers):
    """
    Calculate the sum of squares of given numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Sum of squares of all numbers
    """
    return sum(x ** 2 for x in numbers)


def main():
    print("Sum of Squares Calculator")
    print("=" * 30)
    
    # Get input from user
    user_input = input("Enter numbers separated by spaces: ")
    
    try:
        # Convert input string to list of floats
        numbers = [float(x) for x in user_input.split()]
        
        if not numbers:
            print("No numbers entered!")
            return
        
        # Calculate sum of squares
        result = sum_of_squares(numbers)
        
        # Display the result
        print(f"\nNumbers entered: {numbers}")
        print(f"Sum of squares: {result}")
        print(f"\nCalculation breakdown:")
        for num in numbers:
            print(f"  {num}² = {num ** 2}")
        print(f"  Total = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces.")


if __name__ == "__main__":
    main()

