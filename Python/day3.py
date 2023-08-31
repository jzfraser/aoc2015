def main():
    f = open("../inputs/day3input.txt")
    directns = f.read()
    part1(directns)
    part2(directns)


def part1(directns):
    houses = {}
    houses[(0, 0)] = 1
    x, y = 0, 0
    for d in directns:
        if d == "^":
            y += 1
        elif d == ">":
            x += 1
        elif d == "v":
            y -= 1
        elif d == "<":
            x -= 1
        if (x, y) in houses:
            houses[(x, y)] += 1
        else:
            houses[(x, y)] = 1
    print(len(houses))


def part2(directns):
    houses = {}
    houses[(0, 0)] = 2
    x, y = 0, 0
    x2, y2 = 0, 0
    santasTurn = True
    for d in directns:
        if d == "^":
            if santasTurn:
                y += 1
            else:
                y2 += 1
        elif d == ">":
            if santasTurn:
                x += 1
            else:
                x2 += 1
        elif d == "v":
            if santasTurn:
                y -= 1
            else:
                y2 -= 1
        elif d == "<":
            if santasTurn:
                x -= 1
            else:
                x2 -= 1
        if santasTurn:
            if (x, y) in houses:
                houses[(x, y)] += 1
            else:
                houses[(x, y)] = 1
        else:
            if (x2, y2) in houses:
                houses[(x2, y2)] += 1
            else:
                houses[(x2, y2)] = 1
        santasTurn = not santasTurn
    print(len(houses))


main()
