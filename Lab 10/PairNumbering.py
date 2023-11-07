"""PairNumbering"""
import json
def main():
    """process"""
    dict_a = {}
    dict_b = {}
    list_a = json.loads(input())
    list_b = json.loads(input())
    num_need = int(input())
    list_a.sort()
    list_b.sort()
    for num in list_a:
        dict_a[num] = dict_a.get(num, 0) + 1
    for num in list_b:
        dict_b[num] = dict_b.get(num, 0) + 1
    count = 0
    for i in dict_a:
        if i > num_need:
            break
        else:
            check = num_need - i
            if check in list_b:
                count += (dict_a[i] * dict_b[check])
    print(count)

main()
