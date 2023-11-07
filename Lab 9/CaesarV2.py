"""CaesarV2"""
def main():
    """process"""
    check = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    text = input()
    for i in range(1, 27):
        final_text = ""
        for cha in text:
            if cha.isalpha():
                if cha.isupper():
                    final_text += chr((ord(cha) + i - 65) % 26 + 65)
                else:
                    final_text += chr((ord(cha) + i - 97) % 26 + 97)
            else:
                final_text += cha
        for i in check:
            if i in final_text:
                print(final_text)
                break

main()
