"""Semi Prime"""
def check_num(num):
    """check if prime"""
    check = True
    if num == 1:
        check = False
    elif num == 2:
        check = True
    elif num % 2 == 0:
        check = False
    else:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                check = False
                break
    return check

def main():
    """calculate"""
    num = int(input())
    count = 0
    for current_num in range(4, num + 1):
        if not check_num(current_num): #ถ้าเป็นจำนวนเฉพาะไม่ต้องคิด เพราะเป็น prime x 1
            for first_num in range(2, int(current_num**0.5) + 1):
                if current_num % first_num == 0:
                    second_num = current_num // first_num
                    if check_num(first_num) and check_num(second_num):
                        count += 1
                        break
    print(count)

main()
