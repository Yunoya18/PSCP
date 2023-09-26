"""Distribute"""
def main():
    """calculate"""
    money = int(input())
    num = int(input())
    total = money // 8
    if money < num:
        total = -1
    else:
        if total > num or (total == num and money - (total * 8) != 0): #เงินต้องห้ามเหลือ
            total = num - 1
        elif total < num:
            money -= num
            total = money // 7
            money -= (total * 7)
            if money == 3 and num - total == 1:
                total -= 1
    print(total)

main()
