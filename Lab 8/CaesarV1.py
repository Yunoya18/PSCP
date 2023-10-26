"""CaesarV1"""
def main():
    """process"""
    num = int(input())
    text = input()
    final_text = ""
    for i in text:
        if i.isalpha():
            if i.isupper():
                final_text += chr((ord(i) + num -65) % 26 + 65)
            else:
                final_text += chr((ord(i) + num - 97) % 26 + 97)
        else:
            final_text += i
    print(final_text)

main()
