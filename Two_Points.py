import math


class Point:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2

    def __str__(self):
        return f'({self.point1}, {self.point2})'

    def __add__(self, other):
        return Point(self.point1 + other.point1, self.point2 + other.point2)

    def __sub__(self, other):
        return Point(self.point1 - other.point1, self.point2 - other.point2)

    @property
    def point1(self):
        return self.__p1

    @point1.setter
    def point1(self, new_value):
        self.__p1 = new_value if new_value is not None else 0

    @property
    def point2(self):
        return self.__p2

    @point2.setter
    def point2(self, new_value):
        self.__p2 = new_value if new_value is not None else 0


class Line:
    def __init__(self, p1, p2):
        self.start_point = p1
        self.end_point = p2

    def __str__(self):
        return f'Start Point: ({self.start_point.point1}, {self.start_point.point2})\nEnd Point: ({self.end_point.point1}, {self.end_point.point2})'

    def __len__(self):
        return int(math.sqrt((self.end_point.point1 - self.start_point.point1) ** 2 + (self.end_point.point2 - self.start_point.point2) ** 2))

# Creating objects to test

# p1 = Point(10, 20)
# p2 = Point(30, 40)

# p3 = p1 + p2
# p4 = p2 - p1
# print("Addition:", p3)
# print("Subtraction:", p4)

# length = Line(p1, p2)
# print(length)
# print("Line Length:", len(length))
