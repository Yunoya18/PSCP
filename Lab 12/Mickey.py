"""Mickey"""
def main():
    """process"""
    num = int(input())
    mouse = [int(input()) for _ in range(num)]
    house = [int(input()) for _ in range(num)]
    time = []
    mouse.sort()
    house.sort()
    for i in range(num):
        check = abs(mouse[i] - house[i])
        time.append(check)
    print(max(time))

main()
