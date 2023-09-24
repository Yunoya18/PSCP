"""Diginity"""
def check(num):
    """calculate"""
    total = 0
    for i in str(num):
        total += int(i)
    if len(str(total)) == 1:
        print(total)
    else:
        check(total)

def main():
    """process"""
    while True:
        num = int(input())
        if num == 0:
            break
        check(num)

main()
