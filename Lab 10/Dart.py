"""Dart"""
def main():
    """process"""
    num = int(input())
    total = 0
    for _ in range(num):
        point = input().split()
        point_x, point_y = int(point[0]), int(point[1])
        distance = (point_x**2 + point_y**2)**0.5
        if 0 <= distance <= 2:
            total += 5
        elif 2 < distance <= 4:
            total += 4
        elif 4 < distance <= 6:
            total += 3
        elif 6 < distance <= 8:
            total += 2
        elif 8 < distance <= 10:
            total += 1
    print(total)

main()
