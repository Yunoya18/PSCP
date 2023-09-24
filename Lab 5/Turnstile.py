"""Turnstile"""
def main():
    """process"""
    text = ""
    while True:
        string = input()
        if string == "END":
            break
        else:
            text += string
    total = text.count("CP")
    print(total)

main()
