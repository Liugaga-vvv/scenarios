def uri_count(file_name: str) -> dict[str, int]:
    result = {}
    with open(file_name, "r") as f:
        for line in f.readlines():
            uri, time = line.split(" ")
            if result.get(uri):
                result[uri] = result[uri] + 1
            else:
                result[uri] = 1
    return result
