"""Backward"""
def main():
    """process"""
    text_list = []
    while True:
        text = input()
        if text == "NULL":
            break
        else:
            text_list.append(text)
    for i in reversed(text_list):
        print(i)

main()
