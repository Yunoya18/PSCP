"""Align"""
def main():
    """process"""
    space = int(input())
    align = input()
    text = input()
    num_text = len(text)
    num_space = space - num_text
    if align == "left":
        print(text + " " * num_space)
    elif align == "center":
        if num_space / 2 != num_space // 2:
            print(" " * int((num_space // 2) + 1) + text + " " * int(num_space // 2))
        else:
            print(" " * int(num_space / 2) + text + " " * int((num_space / 2)))
    elif align == "right":
        print(" " * num_space + text)

main()
