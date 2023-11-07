"""IP Address"""
def main():
    """process"""
    text = input().split(".")
    final_text = ""
    if len(text) != 4:
        final_text = "Invalid IPv4 address"
    else:
        for check in text:
            if not check.isnumeric():
                final_text = "Invalid IPv4 address"
                break
            if int(check) < 0 or int(check) > 255:
                final_text = "Invalid IPv4 address"
    if final_text == "":
        text = list(map(int, text))
        print(*text, sep=".")
    else:
        print(final_text)

main()
