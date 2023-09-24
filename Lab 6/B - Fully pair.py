"""B - Fully pair?"""
def main():
    """process"""
    text = input()
    check_text = ""
    for i in reversed(text):
        if i not in check_text:
            check_text += i
        else:
            index = check_text.find(i)
            check_text = check_text[:index] + check_text[index + 1:]
    if len(check_text) == 0:
        print("fully paired")
    else:
        for i in reversed(check_text):
            print(i, end="")

main()
