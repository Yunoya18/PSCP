"""EuclideanDistance"""
def main():
    """process"""
    num = int(input())
    point_nx, point_ny = None, None
    total = 0
    for _ in range(num):
        point = input().split()
        point_x, point_y = int(point[0]), int(point[1])
        if point_nx == None and point_ny == None:
            point_nx, point_ny = point_x, point_y
        else:
            dis = ((point_x - point_nx)**2 + (point_y - point_ny)**2)**0.5
            total += dis
            point_nx, point_ny = point_x, point_y
    print("%.2f" % total)

main()
