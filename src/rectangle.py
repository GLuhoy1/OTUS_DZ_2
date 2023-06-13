from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a: int, b: int, name='rectangle'):
        super().__init__(name)
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("Values must be numeric")
        elif a <= 0 or b <= 0:
            raise ValueError("Rectangle sides lengths must be greater than 0.")
        else:
            self.a = a
            self.b = b

    @property
    def perimeter(self) -> float:
        result_perimeter = round(((self.a * 2) + (self.b * 2)), 2)
        return result_perimeter

    @property
    def area(self) -> float:
        result_area = round((self.a * self.b), 2)
        return result_area
