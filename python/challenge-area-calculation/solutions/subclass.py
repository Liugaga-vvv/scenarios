from shape import Shape


class Circle(Shape):
    def area(self):
        return 3.14 * self.length * self.length


class Square(Shape):
    def area(self):
        return self.length**2
