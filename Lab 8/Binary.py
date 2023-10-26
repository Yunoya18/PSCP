"""Binary"""
def cal_num(num):
    """calculate"""
    if num == 0 or num == 1:
        return str(num)
    else:
        final_num = cal_num(num//2) + str(num % 2)
    return final_num

def main():
    """process"""
    num = int(input())
    print(cal_num(num))

main()
