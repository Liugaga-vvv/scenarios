def cal_area() -> (str, float):
    """
     Get input from command and implement area calculation using the two classes from the previous steps.
    :return: shape_name: the shape of input, one of: square, circle or none
             area: the area of the shape, if not square or circle, return 0
    """
    # TODO: Write your code here
    # Note: Do not change the existing code
    shape_name = None
    area = None
    return shape_name, area


if __name__ == "__main__":
    shape_name, area = cal_area()
    print(f"The area of the {shape_name} is {area}")
