"""MAC"""
def check_1(text):
    """check 1"""
    for i in range(1, len(text)+1):
        if i % 3 == 0:
            if text[i-1] == "-":
                continue
            else:
                return "1"
    return ""

def check_2(text):
    """check 2"""
    for i in range(1, len(text)+1):
        if i % 3 == 0:
            if text[i-1] == ":":
                continue
            else:
                return "2"
    return ""

def check_3(text):
    """check 3"""
    for i in range(1, len(text)+1):
        if i % 5 == 0:
            if text[i-1] == ".":
                continue
            else:
                return "3"
    return ""

def check_hex(text):
    """check hex"""
    for i in text:
        if ord(i) not in range(48, 58)\
            and ord(i) not in range(65, 71)\
            and ord(i) not in range(97, 103)\
            and ord(i) != 45 and ord(i) != 46 and ord(i) != 58:
            return "no"
    return ""

def main():
    """process"""
    text = input()
    check = ""
    another_check = ["-", ":", "."]
    check_text = text.replace("-", "")
    check_text = check_text.replace(":", "")
    check_text = check_text.replace(".", "")
    if len(check_text) == 12:
        if text[-1] in another_check:
            print("ERROR")
        else:
            check += check_hex(text)
            check += check_1(text)
            check += check_2(text)
            check += check_3(text)
            if "23" == check:
                print("VALID 1")
            elif "13" == check:
                print("VALID 2")
            elif "12" == check:
                print("VALID 3")
            else:
                print("ERROR")
    else:
        print("ERROR")

main()
