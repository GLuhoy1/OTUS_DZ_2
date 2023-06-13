import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a: int, b: int, c: int, name='triangle'):
        super().__init__(name)
        if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
            raise TypeError("Values must be numeric")
        elif a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Triangle side lengths must be greater than 0.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle with such sides cannot exist.")
        else:
            self.a = a
            self.b = b
            self.c = c

    @property
    def perimeter(self) -> float:
        result_perimeter = round((self.a + self.b + self.c), 2)
        return result_perimeter

    @property
    def area(self) -> float:
        p = self.perimeter / 2
        result_area = round((math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))), 2)
        return result_area
