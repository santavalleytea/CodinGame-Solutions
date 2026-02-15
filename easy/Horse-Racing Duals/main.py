import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
power = []
for i in range(n):
    pi = int(input())
    power.append(pi)
power.sort()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
closest = power[1] - power[0]
for i in range(2, n):
    diff = power[i] - power[i - 1]
    if diff < closest:
        closest = diff

print(closest)
