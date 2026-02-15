import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp = input().split()
# t: a temperature expressed as an integer ranging from -273 to 5526
if n == 0:
    print(0)
else:
    closest = int(temp[0])
    for i in temp:
        t = int(i)
        if abs(t) < abs(closest):
            closest = t
        elif abs(t) == abs(closest) and t > closest:
            closest = t
    print(closest)
