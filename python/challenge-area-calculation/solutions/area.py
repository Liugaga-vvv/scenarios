from subclass import Circle, Square


def cal_area():
    input_str = input(
        "Please input shape type(1: circle, 2: square) and length with space to split:"
    )
    shape_type, length = input_str.split(" ")
    shape_type = int(shape_type.strip())
    length = float(length.strip())

    shape_name = ""
    area = 0
    if shape_type == 1:
        area = Circle(length).area()
        shape_name = "circle"

    elif shape_type == 2:
        area = Square(length).area()
        shape_name = "square"
    return shape_name, area


if __name__ == "__main__":
    shape_name, area = cal_area()
    print(f"The area of the {shape_name} is {area}")
