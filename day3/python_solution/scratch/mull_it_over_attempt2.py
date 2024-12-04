import re


def read_sort_data(fname: str) -> list[list[str]]:
    list1: list[list[str]] = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            list1.append(line)
    return list1


def check_lines(input: list[list[str]]):
    # print(f"input: {input}")
    total_sum = 0
    for line in input:
        res = find_do(line)
        total_sum += res

    return total_sum


def find_mull(line: str):
    valid = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
    total = sum(int(a) * int(b) for a, b in valid)
    return total


def find_do(line: str):
    do_dont_line = re.split(r"(don't\(\)|do\(\))", line)
    total = find_mull(do_dont_line[0])
    i = 1

    while i < len(do_dont_line) - 1:
        cond = do_dont_line[i]
        seg = do_dont_line[i + 1]
        if cond == "do()":
            total += find_mull(seg)

        i += 2
    return total


def main():
    data = read_sort_data("data.txt")
    res = check_lines(data)
    print(f"Total sum: {res}")
    print("done")


if __name__ == "__main__":
    main()
