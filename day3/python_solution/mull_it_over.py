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
        # print(f"type: {type(line)}, line: {line}")
        sum = check_regex(line)
        # print(sum)
        total_sum += sum
    return total_sum


def check_regex(input: str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    print(matches)
    res = sum(int(a) * int(b) for a, b in matches)
    return res


def main():
    data = read_sort_data("data.txt")
    # print(data)
    res = check_lines(data)
    print(f"res: {res}")


if __name__ == "__main__":
    main()
