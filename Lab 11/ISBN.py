"""ISBN"""
def main():
    """process"""
    text = input()
    text = text.replace("-", "")
    if text[-1] == "X":
        check_num = 10
    else:
        check_num = int(text[-1])
    text = list(text[:-1])
    count = 0
    check = 0
    for i in text:
        check += ((10-count) * int(i))
        count += 1
    check = (-check) % 11
    if check == check_num:
        print("Yes")
    else:
        if check == 10:
            check = "X"
        print("No", check)
 
main()
