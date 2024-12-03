def read_sort_data(fname: str) -> tuple([]):
    list1 = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split(" ")
            list1.append(split_line)
    return list1


def safe_reports(reports: list[str]):
    cnt = 1
    safe_reports = 0
    for report in reports:
        # print(f"Report {cnt}")
        res = safe_difference(report)
        if res:
            safe_reports += 1

    print(f"total safe reports: {safe_reports}")


def safe_difference(report):
    window_size = 1
    tmp_res = []
    for i in range(window_size, len(report)):
        # print(int(report[i - window_size]), int(report[i]))
        diff = int(report[i]) - int(report[i - window_size])
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        tmp_res.append(diff)
        # print(tmp_res)
    is_consistent = check_list_sign(tmp_res)
    if is_consistent:
        return True
    return False


def check_list_sign(lst):
    if all(x > 0 for x in lst) or all(x < 0 for x in lst):
        return True
    return False


def main():
    res = read_sort_data("data.txt")
    safe_reports(res)


if __name__ == "__main__":
    main()
