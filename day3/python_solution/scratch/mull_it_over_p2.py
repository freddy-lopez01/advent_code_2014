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
        # print(f"line: {line}")
        res = check_regex(line)
        sum_tmp = calculate_dos(res)
        print(sum_tmp)
        total_sum += sum_tmp

    return total_sum


def calculate_dos(res_lst: list[str]):
    total_sum = 0
    do = True
    for i in res_lst:
        if i == "don't()":
            print("-----------found a don't--------------")
            do = False
        elif i == "do()":
            print("#####-------found a do-------#####")
            do = True
            continue

        if do:
            pattern = r"mul\((\d+),(\d+)\)"
            matches = re.findall(pattern, i)
            # print(matches)
            res = sum(int(a) * int(b) for a, b in matches)
            print(f"current res: {res}")
            total_sum += res
        else:
            print(f"skipping computation for {i}")
        # print(i)

    return total_sum


def check_regex(input: str):
    mul_pattern = r"mul\((\d+),(\d+)\)"
    # word_pattern = r"\bdo\b|\bdon't\b"
    # word_pattern = r"(?<!\w)(do|don't)(?!\w)"
    word_pattern = r"((do\(\)|don't\(\)))"

    mul_matches = [
        (match.group(), match.start()) for match in re.finditer(mul_pattern, input)
    ]

    word_matches = [
        (match.group(), match.start()) for match in re.finditer(word_pattern, input)
    ]

    combined_matches = mul_matches + word_matches
    combined_matches.sort(key=lambda x: x[1])

    ordered_results = [match[0] for match in combined_matches]
    print(ordered_results)
    return ordered_results


def main():
    data = read_sort_data("data.txt")
    res = check_lines(data)
    print(f"Total sum: {res}")
    print("done")


if __name__ == "__main__":
    main()
