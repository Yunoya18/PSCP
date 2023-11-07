"""PedPonFire"""
def main():
    """process"""
    total = int(input())
    gas_list = []
    count = 0
    for _ in range(total):
        gas_list.append(int(input()))
    need = int(input())
    gas_list.sort()
    gas_dict = {}
    for i in gas_list:
        gas_dict[i] = gas_dict.get(i, 0) + 1
    check_list = []
    for num in gas_dict.keys():
        if num > need:
            break
        check = need - num
        if check not in check_list and check in gas_dict.keys():
            if check == num:
                count += (gas_dict[num] * (gas_dict[num] - 1)) // 2
            else:
                count += (gas_dict[num] * gas_dict[check])
            check_list.append(num)
            check_list.append(check)
    print(count)

main()
