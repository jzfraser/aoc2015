import re

def count(s: str):
    # print(s)
    c_code = len(s)
    # sub with arbitrary char to count as 1
    subbed  = s[1:-1]
    subbed = re.sub(r"\\x..|\\.", "/", subbed)
    c_mem = len(subbed)
    c_encode = len(s) + s.count('"') + s.count("\\") + 2
    return (c_code, c_mem, c_encode)


f = open('day8input.txt')
strings = []
while True:
    string = f.readline().strip()
    if not string:
        break
    # print(string)
    strings.append(string)
f.close()

t_code = 0
t_mem = 0
t_encoded = 0
for s in strings:
    # print(count(s))
    counts = count(s)
    t_code += counts[0]
    t_mem += counts[1]
    t_encoded += counts[2]

print(f"Part 1: {t_code} - {t_mem} = {t_code - t_mem}")
print(f"Part 2: {t_encoded} - {t_code} = {t_encoded - t_code}")
