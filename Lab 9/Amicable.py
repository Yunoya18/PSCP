"""Amicable"""
def main():
    """process"""
    num = int(input())
    amicable = []
    for current_num in range(2, num + 1):
        sum_list = []
        checksum_list = []
        if current_num not in amicable:
            for check in range(1, int(current_num**0.5)):
                if current_num % check == 0:
                    sum_list.append(check)
                    if current_num // check != check and current_num // check != current_num:
                        sum_list.append(current_num//check)
            check_num = sum(sum_list)
            if current_num != check_num:
                for check in range(1, int(check_num**0.5)):
                    if check_num % check == 0:
                        checksum_list.append(check)
                        if check_num // check != check and check_num // check != check_num:
                            checksum_list.append(check_num//check)
                check_pair = sum(checksum_list)
                if check_pair == current_num:
                    amicable.append(current_num)
                    amicable.append(check_num)
    print(sum(amicable))

main()
