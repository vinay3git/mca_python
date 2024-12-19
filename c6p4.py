class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        """Method to calculate the area of the rectangle."""
        return self.length * self.breadth

    def perimeter(self):
        """Method to calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.breadth)


def get_rectangle_dimensions(rect_num):
    """Function to get the dimensions of a rectangle."""
    print(f"\nEnter the dimensions for Rectangle {rect_num}:")
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    return Rectangle(length, breadth)


def compare_rectangles(rect1, rect2):
    """Compare areas of two rectangles."""
    area1 = rect1.area()
    area2 = rect2.area()

    print(f"\nRectangle 1 - Area: {area1} | Perimeter: {rect1.perimeter()}")
    print(f"Rectangle 2 - Area: {area2} | Perimeter: {rect2.perimeter()}")

    if area1 < area2:
        print("\nRectangle 1 has a smaller area than Rectangle 2.")
    elif area1 == area2:
        print("\nRectangle 1 and Rectangle 2 have the same area.")
    else:
        print("\nRectangle 1 has a larger area than Rectangle 2.")


if __name__ == "__main__":
    rect1 = get_rectangle_dimensions(1)
    rect2 = get_rectangle_dimensions(2)
    compare_rectangles(rect1, rect2)
