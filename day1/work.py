def sort_data(fname: str) -> tuple([]):
    list1 = []
    list2 = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split("   ")
            list1.append(int(split_line[0]))
            list2.append(int(split_line[1]))

    # print(sorted(list1))
    # print(sorted(list2))

    return sorted(list1), sorted(list2)


def calculate_distance(l1: list, l2: list) -> int:
    # print(l1, l2)
    total_distance = 0
    for num in range(len(l1)):
        diff = abs(l2[num] - l1[num])
        # print(diff)
        total_distance += diff

    return total_distance


def main():
    l1, l2 = sort_data("input.txt")
    res = calculate_distance(l1, l2)
    print(f"Final Distance: {res}")

    # Correct answer: Final Distance: 1320851


if __name__ == "__main__":
    main()
