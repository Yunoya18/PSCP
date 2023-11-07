"""Antenna"""
import json
def main():
    """process"""
    radius = int(input())
    user = json.loads(input())
    user.sort()
    check = None
    count = 0
    for i in user:
        if check == None:
            count += 1
            check = i
        elif i > check + (radius*2):
            count += 1
            check = i
    print(count)

main()
