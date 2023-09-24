"""Run Length Decoding"""
def main():
    """process"""
    text = input()
    num = ""
    for i in text:
        if i.isnumeric():
            num += i
        else:
            print(i * int(num), end="")
            num = ""

main()
