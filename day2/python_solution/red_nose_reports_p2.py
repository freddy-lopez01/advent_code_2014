def read_sort_data(fname: str) -> list[list[str]]:
    list1: list[list[str]] = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split(" ")
            list1.append(split_line)
    return list1


def safe_reports(reports: list[list[str]]):
    safe_reports: int = 0
    cnt: int = 1
    for report in reports:
        res = safe_difference(report) or problem_dampener(report)
        if res:
            print(f"Report {cnt} is safe")
            safe_reports += 1
        else:
            print(f"Report {cnt} is unsafe")
            print(f"{report}")
        cnt += 1

    print(f"total safe reports: {safe_reports}")


def problem_dampener(lst: list[str]):
    for i in range(len(lst)):
        temp_list = lst[:i] + lst[i + 1 :]
        if safe_difference(temp_list):
            return True
    return False


def safe_difference(report: list[str]):
    increase = True
    decrease = True
    window_size = 1
    for i in range(window_size, len(report)):
        diff = int(report[i]) - int(report[i - window_size])
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        if diff < 0:
            increase = False
        else:
            decrease = False

    return increase or decrease


def main():
    res = read_sort_data("test_input.txt")
    safe_reports(res)


if __name__ == "__main__":
    main()
