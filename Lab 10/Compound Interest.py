"""Compound Interest"""
def main():
    """process"""
    money = int(input())
    interest = float(input())
    year = int(input())
    for _ in range(year):
        money += money * (interest/100)
    print("%.2f" % money)

main()
