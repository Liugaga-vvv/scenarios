def time_statistics(file_name: str) -> tuple[str, float, str, float]:
    result = {}
    with open(file_name, "r") as f:
        for line in f.readlines():
            uri, time = line.split(" ")
            if result.get(uri):
                result[uri].append(float(time.strip()))
            else:
                result[uri] = [float(time.strip())]

    min_uri, min_avg_time = "", 99999
    max_uri, max_avg_time = "", 0
    for k, v in result.items():
        avgTime = sum(v) / len(v)
        if min_avg_time > avgTime:
            min_uri = k
            min_avg_time = avgTime
        if max_avg_time < avgTime:
            max_uri = k
            max_avg_time = avgTime

    return max_uri, max_avg_time, min_uri, min_avg_time
