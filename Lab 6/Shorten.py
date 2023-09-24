"""Shorten"""
def main():
    """process"""
    text = ""
    num1 = 0
    num2 = 0
    while True:
        num = int(input())
        if num == -1:
            break
        if num1 == 0 and num2 == 0:
            num1 = num
            num2 = num
        elif num2 + 1 == num:
            num2 = num
        else:
            if num1 != num2:
                text += str(num1) + "-" + str(num2) + ", "
            else:
                text += str(num1) + ", "
            num1 = num
            num2 = num
    if num1 != 0:
        if num1 != num2:
            text += str(num1) + "-" + str(num2)
        else:
            text += str(num1)
    print(text)

main()
