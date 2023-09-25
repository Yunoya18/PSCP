"""Parity"""
def main():
    """calculate"""
    num = input()
    check = input()
    num_1 = 0
    if check == "Even":
        for i in num:
            if i == "1":
                num_1 += 1
        if num_1 % 2 == 0:
            num += "0"
        else:
            num += "1"
    elif check == "Odd":
        for i in num:
            if i == "1":
                num_1 += 1
        if num_1 % 2 == 0:
            num += "1"
        else:
            num += "0"
    print(num)

main()
