def main():
    print(part1())
    print(part2())


def part1():
    ans = 0
    input = open("../inputs/day1input.txt")
    directions = input.read()
    for c in directions:
        if c == "(":
            ans += 1
        elif c == ")":
            ans -= 1
    return ans


def part2():
    ans = 0
    input = open("../inputs/day1input.txt")
    directions = input.read()
    for i, c in enumerate(directions):
        if c == "(":
            ans += 1
        elif c == ")":
            ans -= 1
        if ans < 0:
            return i + 1


if __name__ == "__main__":
    main()
