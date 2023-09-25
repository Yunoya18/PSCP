"""Netflix"""
import math
def package(total, mobile, basic, standard, premium):
    """print total"""
    if premium != 0:
        print("Premium x", premium)
    if standard != 0:
        print("Standard x", standard)
    if basic != 0:
        print("Basic x", basic)
    if mobile != 0:
        print("Mobile x", mobile)
    print("Total =", total, "THB")

def main():
    """process"""
    mobile = 0
    basic = 0
    standard = 0
    premium = 0
    watch = int(input())
    download = int(input())
    input()
    input()
    laptop_tv = input()
    watch_hd = input()
    ultra_hd = input()
    need = max(watch, download)
    if ultra_hd == "Yes":
        premium += math.ceil(need / 4)
        need = 0
    if watch_hd == "Yes":
        if need % 4 == 0 or need % 4 == 3:
            premium += math.ceil(need / 4)
        else:
            premium += (need // 4)
            standard += 1
        need = 0
    if laptop_tv == "Yes":
        if need % 4 == 0 or need % 4 == 3:
            premium += math.ceil(need / 4)
        elif need % 4 == 2:
            premium += (need // 4)
            standard += 1
        elif need % 4 == 1:
            premium += (need // 4)
            basic += 1
        need = 0
    if need != 0:
        mobile += need
    total = (419 * premium) + (349 * standard) + (279 * basic) + (99 * mobile)
    package(total, mobile, basic, standard, premium)

main()
