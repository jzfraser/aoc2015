def main():
    print(calc_total_amount())


def calc_total_amount():
    f = open("day2input.txt")
    total_wp = 0
    total_r = 0
    while True:
        line = f.readline()
        if line == "":
            break
        l, w, h = line.split("x")
        l = int(l)
        w = int(w)
        h = int(h)
        total_wp += calc_wp_amount(l, w, h)
        total_r += calc_r_amount(l, w, h)
    return (total_wp, total_r)


def calc_wp_amount(l, w, h):
    s1 = l * w
    s2 = w * h
    s3 = h * l
    smallest = min(s1, s2, s3)
    return 2 * s1 + 2 * s2 + 2 * s3 + smallest


def calc_r_amount(l, w, h):
    s = sorted([l, w, h])
    x, y = s[0], s[1]
    len1 = 2 * x + 2 * y
    len2 = l * w * h
    return len1 + len2


if __name__ == "__main__":
    main()
