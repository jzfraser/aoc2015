def part1():
    def is_nice(s) -> bool:
        vowels = 0
        prev = ""
        has_double = False
        for c in s:
            if c == "a":
                vowels += 1
            if c == "e":
                vowels += 1
            if c == "i":
                vowels += 1
            if c == "o":
                vowels += 1
            if c == "u":
                vowels += 1

            if c == prev:
                has_double = True

            if prev == "a" and c == "b":
                return False
            if prev == "c" and c == "d":
                return False
            if prev == "p" and c == "q":
                return False
            if prev == "x" and c == "y":
                return False

            prev = c

        return vowels >= 3 and has_double

    nice_words = 0

    f = open("../inputs/day5input.txt")
    words = f.readlines()
    for word in words:
        stripped = word.strip()
        if is_nice(stripped):
            nice_words += 1
    print(nice_words)


def is_nice(s):
    prev = ""
    prev2 = ""
    # key: (char1, char2) value: (count, array char 2 indices)
    pairs = {}
    has_broken_repeat = False

    for i, c in enumerate(s):
        if prev2 == c:
            has_broken_repeat = True
        if (prev, c) not in pairs.keys():
            pairs[(prev, c)] = (1, [i])
        else:
            (count, indices) = pairs[(prev, c)]
            if i - 1 not in indices:
                pairs[(prev, c)] = (count + 1, indices.append(i))
        prev2 = prev
        prev = c

    has_multi_pair = False
    for pair in pairs.values():
        if pair[0] >= 2:
            has_multi_pair = True

    is_nice = has_multi_pair and has_broken_repeat
    return is_nice


# words = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]

nice_words = 0
f = open("../inputs/day5input.txt")
words = f.readlines()
for word in words:
    stripped = word.strip()
    if is_nice(stripped):
        nice_words += 1
print(nice_words)
