import time


def elapsed_time(start_date, end_date):
    start_time = time.mktime(time.strptime(start_date, "%Y-%m-%d"))
    end_time = time.mktime(time.strptime(end_date, "%Y-%m-%d"))
    elapsed_time = round(int(end_time - start_time) / (24 * 60 * 60))
    return elapsed_time
