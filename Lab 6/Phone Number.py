"""Phone Number"""
def main():
    """process"""
    num = input()
    check = input()
    if len(num) == 9:
        if check == "Domestic":
            print(num[0], num[1:5], num[5:10])
        elif check == "International":
            print("+66", num[1:5], num[5:10])
    elif len(num) == 10:
        if check == "Domestic":
            print(num[0:2], num[2:6], num[6:11])
        elif check == "International":
            print("+66" + num[1], num[2:6], num[6:11])

main()
