from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def get_dimensions(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def get_dimensions(self):
        self.length = float(input("Enter the length of the rectangle: "))
        self.width = float(input("Enter the width of the rectangle: "))

    def calculate_area(self):
        return self.length * self.width

class Triangle(Polygon):
    def get_dimensions(self):
        self.base = float(input("Enter the base of the triangle: "))
        self.height = float(input("Enter the height of the triangle: "))

    def calculate_area(self):
        return 0.5 * self.base * self.height

def main():
    while True:
        print("\nChoose a polygon to calculate area:")
        print("1. Rectangle")
        print("2. Triangle")
        choice = input("Enter your choice (1/2) or 'q' to quit: ")

        if choice == "1":
            rectangle = Rectangle()
            rectangle.get_dimensions()
            area = rectangle.calculate_area()
            print(f"The area of the rectangle is: {area}")
        elif choice == "2":
            triangle = Triangle()
            triangle.get_dimensions()
            area = triangle.calculate_area()
            print(f"The area of the triangle is: {area}")
        elif choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 'q' to quit.")

if __name__ == "__main__":
    main()
