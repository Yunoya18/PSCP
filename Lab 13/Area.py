"""Area"""
def main():
    """process"""
    num = int(input())
    total = 0
    for _ in range(num):
        text = input()
        for i in text:
            if not i.isspace():
                total += 1
    print(total)

main()
