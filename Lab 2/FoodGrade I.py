"""FoodGrade I"""
def check(num):
    """check"""
    if num in range(50, 71):
        return 1
    else:
        return 0

def main():
    """process"""
    total = 0
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    total += check(int(input()))
    print(total)

main()
