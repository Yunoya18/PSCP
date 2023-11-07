"""Poisonous Vegetables"""
def main():
    """process"""
    field = [int(i) for i in input().split(" x ")]
    size = int(input())
    input()
    vegetable = []
    for _ in range(field[0]):
        text = input().strip("[").strip("]")
        text = text.split("][")
        text = [list(map(int, i.split())) for i in text]
        vegetable.append(text)
    for i in range(field[0]):
        for j in range(field[1]):
            if vegetable[i][j][1] > size:
                print("[ - ]", end="")
            elif vegetable[i][j][0] == vegetable[i][j][2]:
                print("[ o ]", end="")
            else:
                print("[ x ]", end="")
        print()

main()
