def put_fruits():
    basket_capacity = 10
    total_weight = 0

    fruits = []
    while total_weight <= basket_capacity:
        try:
            fruit_weight = float(input("Enter the weight of the fruit: "))
        except ValueError:
            continue
        if (total_weight + fruit_weight) > basket_capacity:
            return total_weight, fruits
        else:
            total_weight += fruit_weight
            fruits.append(fruit_weight)

    return total_weight, fruits


if __name__ == "__main__":
    fruits = put_fruits()
    print(fruits)
