"""Brick Bridge"""
def main():
    """calculate"""
    small = int(input())
    big = int(input())
    goal = int(input())
    big_need = goal // 5
    if big_need >= big:
        left = goal - (big*5)
    else:
        left = goal - (big_need*5)
    if left > small:
        small_need = -1
    else:
        small_need = left
    print(small_need)

main()
