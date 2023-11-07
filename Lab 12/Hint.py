"""Hint"""
def check(num, text, current):
    """check"""
    if "==" in text:
        num = list(filter(lambda x: str(x)[current] == text[1], num))
    elif ">" in text:
        num = list(filter(lambda x: str(x)[current] > text[1], num))
    elif "<" in text:
        num = list(filter(lambda x: str(x)[current] < text[1], num))
    elif "<=" in text:
        num = list(filter(lambda x: str(x)[current] <= text[1], num))
    elif ">=" in text:
        num = list(filter(lambda x: str(x)[current] >= text[1], num))
    elif "!=" in text:
        num = list(filter(lambda x: str(x)[current] != text[1], num))
    return num

def main():
    """calculate"""
    num = list(map(lambda x: "%03d" % x, range(1000)))
    for i in reversed(range(3)):
        text = input().split()
        num = check(num, text, i)
    print(*num, sep="\n")

main()
