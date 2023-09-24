"""Harshad Number"""
def check(num):
    """calculate"""
    total = 0
    check_num = abs(num)
    for i in str(check_num):
        total += int(i)
    if num == 0:
        return "No"
    elif num % total == 0:
        return "Yes"
    else:
        return "No"

def main():
    """process"""
    for _ in range(10):
        num = int(input())
        print(check(num))

main()
