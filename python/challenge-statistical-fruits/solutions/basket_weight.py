def basket_weight(basktets):
    total_weights = []
    for basket_name, weights in basktets.items():
        total_weight = sum(weights)
        total_weights.append({"name": basket_name, "weight": total_weight})
    result = sorted(total_weights, key=lambda x: x["weight"], reverse=True)

    return result


if __name__ == "__main__":
    fruits = {
        "apple": [1, 2.3, 4, 5],
        "orange": [3, 4.4, 5.5, 0.4, 0.6, 1.2, 3.2],
        "banana": [4, 5, 6],
    }
    result = basket_weight(fruits)
    for ele in result:
        print(ele["name"], ": ", ele["weight"])
