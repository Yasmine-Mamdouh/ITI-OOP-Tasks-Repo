class Shape:

    count = 0

    def __init__(self, name, dim1, dim2=None):
        self.name = name
        self.dimension1 = dim1
        self.dimension2 = dim2
        Shape.count += 1

    def area_calc(self):
        if self.name.lower() == "square":
            return self.dimension1 ** 2
        elif self.name.lower() == "rectangle":
            return self.dimension1 * self.dimension2
        elif self.name.lower() == "triangle":
            return 0.5 * self.dimension1 * self.dimension2
        elif self.name.lower() == "circle":
            return 3.1416 * (self.dimension1 ** 2)
        else:
            return "Unknown shape"


class Circle(Shape):
    circle_count = 0

    def __init__(self, radius):
        super().__init__("circle", radius)
        Circle.circle_count += 1

    def area_calc(self):
        return 3.1416 * (self.dimension1 ** 2)


class Rectangle(Shape):
    rectangle_count = 0

    def __init__(self, length, width):
        super().__init__("rectangle", length, width)
        Rectangle.rectangle_count += 1

    def area_calc(self):
        return self.dimension1 * self.dimension2


# Creating shape objects

# square = Shape("square", 5)
# triangle = Shape("triangle", 4, 6)
# circle1 = Circle(3)
# circle2 = Circle(5)
# rectangle1 = Rectangle(4, 8)
# rectangle2 = Rectangle(6, 9)

# print(f"Square Area: {square.area_calc()}", '\n')
# print(f"Triangle Area: {triangle.area_calc()}", '\n')
# print(f"Circle 1 Area: {circle1.area_calc()}")
# print(f"Circle 2 Area: {circle2.area_calc()}", '\n')
# print(f"Rectangle 1 Area: {rectangle1.area_calc()}")
# print(f"Rectangle 2 Area: {rectangle2.area_calc()}", '\n')

# print(f"Total Shapes: {Shape.count}")
# print(f"Total Circles: {Circle.circle_count}")
# print(f"Total Rectangles: {Rectangle.rectangle_count}")
