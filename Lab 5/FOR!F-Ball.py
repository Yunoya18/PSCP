"""FOR!F-Ball"""
def main():
    """process"""
    check = input()
    cup_1 = "1"
    cup_2 = "0"
    cup_3 = "0"
    for i in check:
        if i == "A":
            cup_1, cup_2 = cup_2, cup_1
        elif i == "B":
            cup_2, cup_3 = cup_3, cup_2
        elif i == "C":
            cup_1, cup_3 = cup_3, cup_1
    if cup_1 == "1":
        print(1)
    elif cup_2 == "1":
        print(2)
    elif cup_3 == "1":
        print(3)

main()
