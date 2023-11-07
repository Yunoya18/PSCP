"""Factors"""
def main():
    """process"""
    total = int(input())
    for _ in range(total):
        num = int(input())
        divider = {}
        check = True
        text = ""
        while True:
            check_num = num
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    divider[i] = divider.get(i, 0) + 1
                    num = num // i
                    break
            if check_num == num:
                check = False
                divider[num] = divider.get(num, 0) + 1
            if check == False:
                break
        for key, value in divider.items():
            if value > 1:
                text += str(key)+"**"+str(value)+" x "
            else:
                text += str(key)+" x "
        text = text.strip(" x ")
        print(text)

main()
