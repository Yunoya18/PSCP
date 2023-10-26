"""3nPlus1"""
def cal(num, count):
    """calculate"""
    if num == 1:
        return count
    else:
        if num % 2 == 0:
            num /= 2
        else:
            num = (num*3) + 1
        count += 1
    return cal(num, count)

def main():
    """process"""
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            print(cal(num, 1))

main()
