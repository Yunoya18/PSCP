"""GCD_N"""
def gcd(num1, num2):
    """calculate"""
    if num1 == 0 or num2 == 0:
        return max(num1, num2)
    else:
        return gcd(num2, num1%num2)

def main():
    """process"""
    num = int(input())
    check = int(input())
    for _ in range(num - 1):
        num_cal = int(input())
        check, num_cal = max(check, num_cal), min(check, num_cal)
        check = gcd(check, num_cal)
    print(check)

main()
