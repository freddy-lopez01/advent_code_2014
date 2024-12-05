# Define the word search grid
#
import antigravity


def read_sort_data(fname: str) -> list[str]:
    list1: list[str] = []
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            list1.append(line.strip())
    return list1


grid: list[str] = read_sort_data("test_data.txt")

word = "XMAS"
word2 = "MAS"

# Grid dimensions
rows = len(grid)
cols = len(grid[0])


# Function to extract all diagonals from the grid
def extract_diagonals_top_left(grid: list[str]) -> list[str]:
    diagonals: list[str] = []

    for d in range(-(rows - 1), cols):
        # print(f"d: {d}")
        diag: list[str] = []
        for r in range(rows):
            for c in range(cols):
                # print(f"r: {r}    c: {c}")
                if r - c == d:
                    # print(f"grid[{r}][{c}]: {grid[r][c]}")
                    diag.append(grid[r][c])
        if diag:
            diagonals.append("".join(diag))
            # print(diagonals)

    # print(f"diagonals: {diagonals}")

    return diagonals


def extract_diagonals_top_right(grid: list[str]) -> list[str]:
    anti_diagonals: list[str] = []

    for d in range(rows + cols - 1):
        anti_diag: list[str] = []
        for r in range(rows):
            for c in range(cols):
                if r + c == d:
                    anti_diag.append(grid[r][c])
        if anti_diag:
            anti_diagonals.append("".join(anti_diag))

    # print(f"diagonals: {anti_diagonals}")

    return anti_diagonals


def count_in_line(line: str, word: str) -> int:
    count = 0
    word_len = len(word)
    reverse_word = word[::-1]

    for i in range(len(line) - word_len + 1):
        # print(line[i : i + word_len])
        if (line[i : i + word_len] == word) or (line[i : i + word_len] == reverse_word):
            count += 1
    return count


def check_veritcally():
    # print(cols)
    count = 0
    for c in range(cols):
        column = ""
        for r in range(rows):
            column += grid[r][c]
            # print(column)
        # print(f"final built column string for column {c}:")
        # print(column)
        # print("\n")
        count += count_in_line(column, word)
    return count


def check_for_X_mas(diagonals: list[str], anti_diagonals: list[str]):
    i = 1
    total_xmas = 0
    for i in range(len(diagonals)):
        print(diagonals[i])
        anti = anti_diagonals[i - 1]
        print(anti[::-1])
        print("\n")
        dia_count = count_in_line(diagonals[i], word2)
        dia_rev_count = count_in_line(anti_diagonals[i - 1], word2)
        xmas_count = min(dia_count, dia_rev_count)
        total_xmas += xmas_count
    return total_xmas


def main():
    # Total occurrences of the word
    total_count = 0

    # Check horizontally
    print(grid)
    for line in grid:
        print(line)
    for row in grid:
        total_count += count_in_line(row, word)

    # Check vertically
    total_count += check_veritcally()

    # Check diagonals
    diagonals = extract_diagonals_top_left(grid)
    anti_diagonals = extract_diagonals_top_right(grid)

    print(diagonals)
    print(anti_diagonals)

    # part 1
    for diagonal in diagonals + anti_diagonals:
        total_count += count_in_line(diagonal, word)
    print(f"part1: {total_count}")
    #
    # part2
    mas_total = check_for_X_mas(diagonals, anti_diagonals)
    print(f"part2: {mas_total}")


if __name__ == "__main__":
    main()
