import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
m = int(input())
signals = {}
for i in range(n):
    input_name, input_signal = input().split()
    signals[input_name] = input_signal
output = []
for i in range(m):
    output_name, _type, input_name1, input_name2 = input().split()
    output.append((output_name, _type, input_name1, input_name2))

for i in range(m):
    output_name, _type, input_name1, input_name2 = output[i]
    s1 = signals[input_name1]
    s2 = signals[input_name2]
    output_signal = []
    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    for a,b in zip(s1,s2):
        if _type == "AND":
            output_signal.append('-' if (a == '-' and b == '-') else '_')
        elif _type == "OR":
            output_signal.append('-' if (a == '-' or b == '-') else '_')
        elif _type == "XOR":
            output_signal.append('-' if (a != b) else '_')
        elif _type == "NAND":
            output_signal.append('_' if (a == '-' and b == '-') else '-')
        elif _type == "NOR":
            output_signal.append('_' if (a == '-' or b == '-') else '-')
        elif _type == "NXOR":
            output_signal.append('_' if (a != b) else '-')
        else:
            output_signal.append('_')

    print(output_name, "".join(output_signal))
