"""BishopMove"""
ROW_, COL_ = int(input()), int(input())
def check(direction, current, position, another, enemy):
    """check each direction"""
    while True:
        if current[0] not in range(0, ROW_) and current[1] not in range(0, COL_):
            break
        if current == another:
            if another == position and enemy == True:
                return True
            else:
                return False
        if current == position:
            return True
        current = (current[0]+direction[0], current[1]+direction[1])

def main():
    """process"""
    bishop = (int(input()), int(input()))
    another = (int(input()), int(input()))
    enemy = True if int(input()) == 1 else False
    position = (int(input()), int(input()))
    direction = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    check_direc = []
    for i in direction:
        check_direc.append(check(i, bishop, position, another, enemy))
        if True in check_direc:
            break
    if True in check_direc:
        print("Yes")
    else:
        print("No")

main()
