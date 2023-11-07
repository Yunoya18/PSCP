"""Guess"""
def main():
    """process"""
    num = list(range(101))
    while True:
        text = input()
        if text == "END":
            break
        text = text.split()
        if ">" in text:
            if "YES" in text:
                num = list(filter(lambda x: x > int(text[1]), num))
            else:
                num = list(filter(lambda x: x <= int(text[1]), num))
        elif "<" in text:
            if "YES" in text:
                num = list(filter(lambda x: x < int(text[1]), num))
            else:
                num = list(filter(lambda x: x >= int(text[1]), num))
        else:
            if "YES" in text:
                num = list(filter(lambda x: x == int(text[1]), num))
            else:
                num = list(filter(lambda x: x != int(text[1]), num))
    print(*num, sep=" ")

main()
