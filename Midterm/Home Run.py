"""Home Run"""
def main():
    """calculate"""
    num = int(input())
    ball = float(input())
    total = 0
    for _ in range(num):
        lenght = float(input())
        if ball > lenght:
            total += 1
    print(total)

main()
