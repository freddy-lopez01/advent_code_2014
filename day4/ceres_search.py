import re
from sre_parse import parse


def read_sort_data(fname: str) -> list[list[str]]:
    list1: list[list[str]] = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            list1.append(line.strip())
    return list1


def create_matrix(data: list[list[str]]) -> list[list[str]]:
    matrix: list[list[str]] = []
    for line in data:
        tmp_matrix = []
        for char in line:
            tmp_matrix.append(char)

        matrix.append(tmp_matrix)

    return matrix


def parse_matrix(matrix: list[list[str]]):
    size = len(matrix)
    letters = ["X", "M", "A", "S"]

    index = 0
    current_letter = letters[index]
    print(f"Starting letter for the word search: {current_letter}")

    for i in range(size):
        # print(i)
        for j in range(size):
            # print(j)
            curr_char = matrix[i][j]
            print(matrix[i][j])
            if curr_char == current_letter:
                print("found first letter")

        if i == 2:
            break


def main():
    data = read_sort_data("test_data.txt")
    letter_matrix = create_matrix(data)
    for row in letter_matrix:
        print(row)
    parse_matrix(letter_matrix)


if __name__ == "__main__":
    main()
