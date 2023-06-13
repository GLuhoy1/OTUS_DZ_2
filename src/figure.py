class Figure:
    def __init__(self, name):
        if name is None:
            raise ValueError("Please input name")
        self.name = name

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument must be a geometric figure.")
        return round((self.area + figure.area), 2)

    def add_perimeter(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument must be a geometric figure.")
        return round((self.perimeter + figure.perimeter), 2)
