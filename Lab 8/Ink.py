"""Ink"""
import math
def main():
    """process"""
    line1 = input().split()
    area_per = int(line1[0])
    num = int(line1[1])
    for _ in range(num):
        point = input().split()
        num_x = int(point[0])
        num_y = int(point[1])
        distance = (num_x**2 + num_y**2)**0.5
        area = 3.1416 * (distance**2)
        second = math.ceil(area / area_per)
        print(second)

main()
