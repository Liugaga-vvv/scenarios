def read_log(file_name: str) -> int:
    # TODO: implement this function
    # Note: Do not change the existing code
    line_count = 0

    with open(file_name, "r") as f:
        for line in f.readlines():
            print(line)
            line_count += 1
    return line_count
