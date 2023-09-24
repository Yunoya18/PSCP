"""One For All"""
def main():
    """process"""
    num = int(input())
    text = ""
    for i in range(1, num + 1):
        name = input()
        text += name
        if i == num:
            text += "_"
            text += str(i)
        elif i % 2 == 0:
            text += ("-" * i)
        else:
            text += ("*" * i)
    print(text)

main()
