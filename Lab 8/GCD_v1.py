"""GCD_v1"""
def gcd(num1, num2):
    """calculate"""
    if num1 == 0 or num2 == 0:
        return max(num1, num2)
    else:
        return gcd(num2, num1%num2)

def main():
    """process"""
    num1 = int(input())
    num2 = int(input())
    num1, num2 = max(num1, num2), min(num1, num2)
    print(gcd(num1, num2))

main()
