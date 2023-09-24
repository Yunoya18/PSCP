"""Stair"""
def main():
    """process"""
    maximum = int(input())
    total_step = int(input())
    total = 0
    count = 0
    for _ in range(total_step):
        num = int(input())
        if num > maximum:
            count = "NO"
            break
        else:
            total += num
            if total == maximum:
                count += 1
                total = 0
            elif total > maximum:
                count += 1
                total = num
    if isinstance(count, str) == False:
        if total != 0:
            count += 1
    print(count)

main()
