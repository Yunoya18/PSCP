"""Safe"""
def main():
    """process"""
    text1 = input()
    text2 = input()
    total = 0
    for i in range(len(text2)):
        to_right = abs(ord(text1[i]) - ord(text2[i]))
        to_left = 26 - to_right
        check = min(to_right, to_left)
        total += check
    print(total)

main()
