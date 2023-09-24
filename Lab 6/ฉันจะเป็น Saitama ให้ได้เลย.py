"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """calculate"""
    req_one = int(input())
    req_two = int(input())
    req_three = int(input())
    req_four = int(input())
    per_one = int(input())
    per_two = int(input())
    per_three = int(input())
    per_four = int(input())
    day_one = math.ceil(req_one/per_one)
    day_two = math.ceil(req_two/per_two)
    day_three = math.ceil(req_three/per_four)
    day_four = math.ceil(req_four/per_three)
    if day_two > day_one:
        day_one = day_two
    if day_three > day_one:
        day_one = day_three
    if day_four > day_one:
        day_one = day_four
    print(day_one)

main()
