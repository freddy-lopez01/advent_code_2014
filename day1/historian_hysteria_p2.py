def sort_data(fname: str) -> tuple([]):
    list1 = []
    list2 = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            split_line = line.strip().split("   ")
            list1.append(int(split_line[0]))
            list2.append(int(split_line[1]))

    return sorted(list1), sorted(list2)


def count_occurances(list1: list) -> dict:
    occurance_dic = {}

    for num in list1:
        # print(f"Num: {num}")
        if num not in occurance_dic:
            occurance_dic[num] = 0
        occurance_dic[num] += 1

    return occurance_dic


def mult_values(list1: list, dict1: dict) -> int:
    total_sum = 0
    for num in list1:
        if num not in dict1:
            continue
        product = num * dict1[num]
        total_sum += product

    return total_sum


def main():
    l1, l2 = sort_data("input.txt")
    res_dict = count_occurances(l2)
    res_product = mult_values(l1, res_dict)

    print(f"res_product: {res_product}")


if __name__ == "__main__":
    main()
