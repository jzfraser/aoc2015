from typing import List, Tuple

f = open("day6input.txt")
instructions = f.readlines()


def get_coords(words: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    lpair = words[0].split(",")
    x1, y1 = int(lpair[0]), int(lpair[1])
    rpair = words[2].split(",")
    x2, y2 = int(rpair[0]), int(rpair[1])
    return ((x1, y1), (x2, y2))


def part_1():
    light_grid = [[False for col in range(1000)] for row in range(1000)]

    for line in instructions:
        words = line.strip().split(" ")
        action = words[0]
        coords = ((0, 0), (0, 0))
        if action == "toggle":
            coords = get_coords(words[1:])
        elif action == "turn":
            action = words[1]
            coords = get_coords(words[2:])
        x1, y1 = coords[0]
        x2, y2 = coords[1]
        for row in range(x1, x2 + 1):
            for col in range(y1, y2 + 1):
                if action == "toggle":
                    light_grid[row][col] = not light_grid[row][col]
                elif action == "on":
                    light_grid[row][col] = True
                elif action == "off":
                    light_grid[row][col] = False

    lights_on = 0

    for row in light_grid:
        for col in row:
            if col:
                lights_on += 1

    print(lights_on)


light_grid = [[0 for col in range(1000)] for row in range(1000)]

for line in instructions:
    words = line.strip().split(" ")
    action = words[0]
    coords = ((0, 0), (0, 0))
    if action == "toggle":
        coords = get_coords(words[1:])
    elif action == "turn":
        action = words[1]
        coords = get_coords(words[2:])
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    for row in range(x1, x2 + 1):
        for col in range(y1, y2 + 1):
            if action == "toggle":
                light_grid[row][col] += 2
            elif action == "on":
                light_grid[row][col] += 1
            elif action == "off":
                light_grid[row][col] = max(0, light_grid[row][col] - 1)

total_brightness = 0
for row in light_grid:
    for col in row:
        total_brightness += col

print(total_brightness)
