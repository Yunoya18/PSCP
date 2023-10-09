"""Easy Histogram"""
def check(text):
    """check"""
    if text.isupper():
        return ord(text.lower()) + 0.5
    else:
        return ord(text)

def main():
    """process"""
    text = input()
    all_text = {}
    for i in text:
        if i.isalpha():
            all_text[i] = all_text.get(i, 0) + 1
    text_list = list(all_text)
    text_list.sort(key=check)
    for cha in text_list:
        print(cha, "=", all_text[cha])

main()
