def sort_data(fname: str) -> tuple([]):
    """
    sort_data(fname) takes in a file name and reads the contents of the file and formats the two integers on each line into two lists: list1 and list2
    It then process each number and removes any empty space and the new line characters if applicable and then converts the str into an int so mathmatical
    operations can be performed using the data in later functions
    """
    list1 = []
    list2 = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split("   ")
            list1.append(int(split_line[0]))
            list2.append(int(split_line[1]))

    return sorted(list1), sorted(list2)


def calculate_distance(l1: list, l2: list) -> int:
    """
    calculate_distance(l1, l2) takes in two lists and finds the difference between the two numbers in the same index of both lists. Then, to account for any possible negative evaluations, I take that diff
    and perform a abs() operation to ensure a positive result
    """
    total_distance = 0
    for num in range(len(l1)):
        diff = abs(l2[num] - l1[num])
        total_distance += diff
    return total_distance


def main():
    l1, l2 = sort_data("input.txt")
    res = calculate_distance(l1, l2)
    print(f"Final Distance: {res}")

    # Correct answer: Final Distance: 1320851


if __name__ == "__main__":
    main()
