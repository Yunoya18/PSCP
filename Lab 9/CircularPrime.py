"""CircularPrime"""
def change(num):
    """change order"""
    num = int(num[1:] + num[0])
    return num

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
    """process"""
    num_need = int(input())
    circular = []
    for current_num in range(2, num_need + 1):
        check = True
        num = current_num
        if current_num not in circular:
            check_list = [current_num]
            for _ in range(len(str(current_num))): #เช็คเลขที่สลับได้ทั้งหมด
                need = len(str(current_num)) - len(str(num))
                num = change(("0" * need) + str(num))
                if num not in check_list:
                    check_list.append(num)
            copy_checklist = check_list.copy()
            for i in check_list:
                if not check_num(i): #เช็คว่าเป็นจำนวนเฉพาะมั้ย
                    check = False
                    break
                else:
                    if i > num_need or i in circular: #เช็คว่าเลขที่สลับมาเกินที่อยากได้มั้ย
                        copy_checklist.remove(i)
            check_list = copy_checklist
            if check:
                circular.extend(check_list)
    print(sum(circular))

main()
