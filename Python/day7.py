import numpy as np

# part 1
# f = open("day7input.txt")
# part 2
f = open("../inputs/day7input_part2.txt")

instructions = f.readlines()
signals = {}


def load_instructions():
    for line in instructions:
        parts = [p.strip() for p in line.strip().split("->")]
        inputs = parts[0]
        output = parts[1]

        if output not in signals.keys():
            if inputs.isnumeric():
                signals[output] = np.uint16(int(inputs))
            else:
                signals[output] = inputs


def solve_circuit_for(wire) -> np.uint16:
    input = signals[wire]
    if type(input) is np.uint16:
        return input
    else:
        terms = input.split(" ")
        if len(terms) == 1:
            term = terms[0]
            signals[wire] = solve_circuit_for(term)
        elif len(terms) == 2:
            term = terms[1]
            if term.isnumeric():
                signals[wire] = ~np.uint16(int(term))
            else:
                if type(signals[term]) is np.uint16:
                    signals[wire] = ~signals[term]
                else:
                    signals[wire] = ~solve_circuit_for(term)
        elif len(terms) == 3:
            gate = terms[1]
            in1 = terms[0]
            in2 = terms[2]
            if in1.isnumeric():
                in1 = np.uint16(int(in1))
            else:
                in1 = solve_circuit_for(in1)
            if in2.isnumeric():
                in2 = np.uint16(int(in2))
            else:
                in2 = solve_circuit_for(in2)
            if gate == "AND":
                signals[wire] = in1 & in2
            elif gate == "OR":
                signals[wire] = in1 | in2
            elif gate == "LSHIFT":
                signals[wire] = in1 << in2
            elif gate == "RSHIFT":
                signals[wire] = in1 >> in2
    return signals[wire]


load_instructions()
ans = solve_circuit_for("a")
print(ans)
