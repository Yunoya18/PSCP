"""Bonus"""
def main():
    """calculate"""
    salary = int(input())
    year = int(input())
    month = int(input())
    if month >= 10:
        year += 1
    total = salary * year
    if total > salary * 20:
        total = salary * 20
    if total > 1000000:
        total = 1000000
    elif total < 5000:
        total = 5000
    print(total)

main()
