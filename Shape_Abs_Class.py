from abc import ABC, abstractmethod


class Shape(ABC):
    count = 0

    def __init__(self, name, dim1, dim2=None):
        self.name = name
        self.dimension1 = dim1
        self.dimension2 = dim2
        Shape.count += 1

    @abstractmethod
    def area_calc(self):
        pass


class Triangle(Shape):
    triangle_count = 0

    def __init__(self, base, height):
        super().__init__("Triangle", base, height)
        Triangle.triangle_count += 1

    def area_calc(self):
        return 0.5 * self.dimension1 * self.dimension2

# Creating an object to test

triangle = Triangle(10, 5)
print(f"Triangle Area: {triangle.area_calc()}")
