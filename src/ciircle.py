import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, r: int, name='circle'):
        super().__init__(name)
        if isinstance(r, str):
            raise TypeError("Values must be numeric")
        elif r <= 0:
            raise ValueError("Circle radius lengths must be greater than 0.")
        else:
            self.r = r

    @property
    def perimeter(self) -> float:
        result_perimeter = round((math.pi * self.r * 2), 2)
        return result_perimeter

    @property
    def area(self) -> float:
        result_area = round((math.pi * (self.r ** 2)), 2)
        return result_area
