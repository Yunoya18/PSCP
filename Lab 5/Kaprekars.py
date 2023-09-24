"""Kaprekars"""
def cal_num(num):
    """find highest and lowest"""
    num1 = num[0]
    num2 = num[1]
    num3 = num[2]
    num4 = num[3]
    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num1 < num4:
        num1, num4 = num4, num1
    if num2 < num3:
        num2, num3 = num3, num2
    if num2 < num4:
        num2, num4 = num4, num2
    if num3 < num4:
        num3, num4 = num4, num3
    return num1, num2, num3, num4

def kaprekar(num, count):
    """check"""
    if num == "6174":
        return count
    else:
        count += 1
        num1, num2, num3, num4 = cal_num(num)
        highest = int(num1 + num2 + num3 + num4)
        lowest = int(num4 + num3 + num2 + num1)
        new_num = highest - lowest
        new_num = "%04d" % new_num
    return kaprekar(new_num, count)

def main():
    """process"""
    num = int(input())
    num = "%04d" % num
    total = kaprekar(num, 0)
    print(total)

main()
