"""Ball"""
def main():
    """"calculate"""
    num = float(input())
    count = 0
    while True:
        num *= 60/100
        if num < 0.01:
            break
        else:
            count += 1
    print(count)

main()
