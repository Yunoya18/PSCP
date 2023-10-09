"""PickThem"""
import json
def main():
    """process"""
    num_list = input()
    num_list = json.loads(num_list)
    count = 0
    for i in num_list:
        if int(i) % 2 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")

main()
