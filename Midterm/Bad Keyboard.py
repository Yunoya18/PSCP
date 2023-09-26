"""Bad Keyboard"""
def main():
    """process"""
    text = input()
    final_text = ""
    for i in text:
        if i == "o":
            final_text += "i"
        elif i == "O":
            final_text += "I"
        elif i == "i":
            final_text += "o"
        elif i == "I":
            final_text += "O"
        else:
            final_text += i
    print(final_text)

main()
