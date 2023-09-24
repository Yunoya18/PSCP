"""SumOfNumber"""
def main():
    """calculate"""
    num_total = int(input())
    total = 0
    while True:
        num = int(input())
        if num == -1:
            break
        total += num
        if total == num_total:
            break
    print(total)

main()
