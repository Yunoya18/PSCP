"""Inverter"""
def main():
    """process"""
    text = input()
    final_text = ""
    for i in text:
        if i == "0":
            final_text += "1"
        elif i == "1":
            final_text += "0"
    print(final_text.lstrip("0"))

main()
