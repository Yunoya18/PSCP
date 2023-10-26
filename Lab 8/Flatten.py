"""Flatten"""
import json
def check(num):
    """check"""
    num_list = []
    for i in num:
        if isinstance(i, list):
            num_list.extend(check(i))
        else:
            num_list.append(i)
    return num_list

def main():
    """process"""
    num_list = json.loads(input())
    final_list = check(num_list)
    final_list.sort(reverse=True)
    print(final_list)

main()
