"""VerticalHistogram"""
def check(text):
    """sort"""
    if text.islower():
        return ord(text)
    else:
        return ord(text) + 58 #ให้เกินค่าของ z

def histo(text_dict):
    """print histogram"""
    for i in reversed(range(1, max(text_dict.values())+1)):
        print("%03d" % int(i), end=" ")
        for j in text_dict.values():
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print("    ", end="")
    print(*text_dict)


def main():
    """process"""
    text = input()
    all_text = {}
    for i in text:
        if i.isalpha():
            all_text[i] = all_text.get(i, 0) + 1
    text_list = list(all_text)
    text_list.sort(key=check)
    text_dict = {}
    for cha in text_list:
        text_dict[cha] = all_text[cha]
    histo(text_dict)

main()
