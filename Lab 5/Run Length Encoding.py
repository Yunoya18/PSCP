"""Run Length Encoding"""
def main():
    """process"""
    text = input()
    count = 1
    final_text = ""
    if len(text) == 1:
        final_text = str(count) + text
    else:
        check = text[0]
        text = text[1:]
        while True:
            if check == text[0]:
                count += 1
            else:
                final_text += str(count)
                final_text += check
                check = text[0]
                count = 1
            if len(text) == 1:
                final_text += str(count)
                final_text += check
                break
            else:
                text = text[1:]
    print(final_text)

main()
