"""Difference"""
import json
def main():
    """process"""
    dict_a = {}
    dict_b = {}
    count = 0
    for i in json.loads(input()):
        dict_a[i] = dict_a.get(i, 0) + 1
    for i in json.loads(input()):
        dict_b[i] = dict_b.get(i, 0) + 1
    check_list = set(dict_a).union(set(dict_b))
    for text in sorted(check_list):
        check = abs(dict_a.get(text, 0) - dict_b.get(text, 0))
        if check != 0:
            print(text, check)
            count += 1
    if count == 0:
        print("ONAJI DAYO!")

main()
