"""Sequence XXX"""
def main():
    """process"""
    row = int(input())
    num = int(input())
    for i in range(row):
        text = ""
        for j in range(row):
            if i == 0 or i == row - 1:
                text += "*"
            elif j == 0 or j == row - 1:
                text += "*"
            elif j == i:
                text += "*"
            elif j == row - i - 1:
                text += "*"
            else:
                text += " "
        text += " "
        print(text * num)

main()
