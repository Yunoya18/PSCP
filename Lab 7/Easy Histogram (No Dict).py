"""Easy Histogram (No Dict)"""
def check(text):
    """check"""
    if text.isupper():
        return ord(text.lower()) + 0.5
    else:
        return ord(text)

def main():
    """process"""
    text = input()
    text_list = []
    for cha in text:
        if cha.isalpha():
            text_list.append(cha)
    text_list.sort(key=check)
    check_list = []
    for i in text_list:
        if i in check_list:
            check_list[check_list.index(i) + 1] += 1
        else:
            check_list.append(i)
            check_list.append(1)
    for j in range(0, len(check_list), 2):
        print(check_list[j], "=", check_list[j+1])

main()
