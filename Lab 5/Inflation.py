"""Inflation"""
def main():
    """calculate"""
    money = float(input())
    year = int(input())
    money = int(money * 100) #ขยับเลขไปอีกสองตำแหน่งแล้วมาหารทีหลัง
    for _ in range(year):
        addition = money * 381
        money += (addition // 10000)
    print("%d.%02d" % (money//100, money%100))

main()
