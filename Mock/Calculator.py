"""Calculator"""
def main():
    """calculate"""
    num = int(input())
    text = ""
    count = 0
    if num == 1:
        count = 1
    else:
        for i in range(1, num+1):
            text += str(i)
            if i == num:
                text += "="
            else:
                text += "+"
        for _ in text:
            count += 1
    print(count)

main()
