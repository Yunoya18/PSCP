"""Longer"""
import math
def main():
    """calculate"""
    radius = float(input())
    num_a = float(input())
    num_b = float(input())
    circle = 2 * math.pi * radius
    rec = (num_a + num_b) * 2
    diff = abs(circle - rec)
    if circle > rec:
        print("Circle is longer")
        print("%.5f" % diff)
    elif circle < rec:
        print("Rectangle is longer")
        print("%.5f" % diff)
    else:
        print("Equal")
        print("%.5f" % diff)

main()
