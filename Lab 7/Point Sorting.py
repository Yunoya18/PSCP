"""Point Sorting"""
def num_sort(point):
    """sort point"""
    return (int(point[0]) + int(point[1]), -int(point[1]))

def main():
    """calculate"""
    num_set = int(input())
    for _ in range(num_set):
        point_list = []
        subset = int(input())
        for _ in range(subset):
            point = input()
            point_num = point.split()
            point = tuple(point_num)
            point_list.append(point)
        point_list.sort(key=num_sort)
        for i in point_list:
            print(*i, sep=" ")

main()
