from re import findall


def read_file_and_do_mult(file_name: str):
    with open(file_name, "r") as file:
        total1 = 0
        total2 = 0
        enabled = True
        line = file.read()

        for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
            # print(f"a: {a}")
            # print(f"b: {b}")
            # print(f"do: {do}")
            # print(f"dont: {dont}")
            if do or dont:
                enabled = bool(do)
                if do:
                    print(do)
                if dont:
                    print(dont)
                print(enabled)
            else:
                x = int(a) * int(b)
                total1 += x
                total2 += x * enabled

        print(f"Part1: {total1}")
        print(f"Part2: {total2}")

def main():
    file_name = "data.txt"
    read_file_and_do_mult(file_name)

if __name__ == "__main__":
    main()
