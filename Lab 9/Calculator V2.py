"""Calculator V2"""
def main():
    """process"""
    num = int(input())
    total = 0
    if num == 1:
        total = 1
    else:
        for i in reversed(range(1, len(str(num))+1)):
            total += (num - 10**(i-1) + 1) * (i+1)
            num = 10**(i-1) - 1
    print(total)

main()
