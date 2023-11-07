"""Island"""
def check(i, j, island, row, col):
    """check"""
    if island[i][j] == 1:
        island[i][j] = "x"
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        check_position = [(i+x, j+y) for x, y in direction]
        for point_x, point_y in check_position:
            if 0 <= point_x < row and 0 <= point_y < col:
                check(point_x, point_y, island, row, col)
        return 1
    return 0

def main():
    """process"""
    row, col = [int(i) for i in input().split()]
    island = [[int(i) for i in input().split()] for _ in range(row)]
    total = 0
    for i in range(row):
        for j in range(col):
            total += check(i, j, island, row, col)
    print(total)

main()
