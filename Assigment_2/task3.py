import math

def calculate_area(shape, dimensions):
  """
  Calculates the area of various shapes.

  Args:
    shape: A string representing the shape ('circle', 'square', 'rectangle', 'triangle').
    dimensions: A dictionary containing the necessary dimensions for the shape.

  Returns:
    The calculated area, or None if the shape is not supported or dimensions are missing.
  """
  shape = shape.lower()
  if shape == 'circle' and 'radius' in dimensions:
    return math.pi * (dimensions['radius'] ** 2)
  elif shape == 'square' and 'side' in dimensions:
    return dimensions['side'] * dimensions['side']
  elif shape == 'rectangle' and 'length' in dimensions and 'width' in dimensions:
    return dimensions['length'] * dimensions['width']
  elif shape == 'triangle' and 'base' in dimensions and 'height' in dimensions:
    return 0.5 * dimensions['base'] * dimensions['height']
  else:
    print(f"Error: Unsupported shape '{shape}' or missing dimensions.")
    return None

# Example usage with input and output:
shape_input = input("Enter the shape (circle, square, rectangle, triangle): ").lower()
dimensions_input = {}

if shape_input == 'circle':
  try:
    radius_input = float(input("Enter the radius: "))
    dimensions_input['radius'] = radius_input
  except ValueError:
    print("Invalid input. Please enter a number.")
elif shape_input == 'square':
  try:
    side_input = float(input("Enter the side length: "))
    dimensions_input['side'] = side_input
  except ValueError:
    print("Invalid input. Please enter a number.")
elif shape_input == 'rectangle':
  try:
    length_input = float(input("Enter the length: "))
    width_input = float(input("Enter the width: "))
    dimensions_input['length'] = length_input
    dimensions_input['width'] = width_input
  except ValueError:
    print("Invalid input. Please enter numbers.")
elif shape_input == 'triangle':
  try:
    base_input = float(input("Enter the base: "))
    height_input = float(input("Enter the height: "))
    dimensions_input['base'] = base_input
    dimensions_input['height'] = height_input
  except ValueError:
    print("Invalid input. Please enter numbers.")

area = calculate_area(shape_input, dimensions_input)

if area is not None:
  print(f"The area of the {shape_input} is: {area}")