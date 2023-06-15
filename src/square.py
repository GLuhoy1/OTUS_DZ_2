from src.figure import Figure


class Square(Figure):
    def __init__(self, a: int, name='square'):
        super().__init__(name)
        if isinstance(a, str):
            raise TypeError("Values must be numeric")
        elif a <= 0:
            raise ValueError("Square side lengths must be greater than 0.")
        else:
            self.a = a

    @property
    def perimeter(self) -> float:
        result_perimeter = round((self.a * 4), 2)
        return result_perimeter

    @property
    def area(self) -> float:
        result_area = round((self.a ** 2), 2)
        return result_area
