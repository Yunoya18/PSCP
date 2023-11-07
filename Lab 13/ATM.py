"""ATM"""
def main():
    """calculate"""
    total = int(input())
    while True:
        text = input()
        if text == "END":
            break
        else:
            check = text.split()
            if check[0] == "D":
                total += int(check[1])
            elif check[0] == "W":
                total = max(0, total - int(check[1]))
    print(total)

main()
