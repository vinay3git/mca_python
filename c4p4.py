# Lambda function for area of a square
area_square = lambda side: side * side

# Lambda function for area of a rectangle
area_rectangle = lambda length, width: length * width

# Lambda function for area of a triangle
area_triangle = lambda base, height: 0.5 * base * height

# Example usage
side = float(input("Enter the side length of the square: "))
print("Area of square:", area_square(side))

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of rectangle:", area_rectangle(length, width))

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
print("Area of triangle:", area_triangle(base, height))
