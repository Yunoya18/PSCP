"""Safe"""
def main():
    """process"""
    text1 = input()
    text2 = input()
    total = 0
    for i in range(len(text2)):
        to_left = abs(ord(text1[i]) - ord(text2[i]))
        to_right = 26 - abs(ord(text1[i]) - ord(text2[i]))
        check = min(to_left, to_right)
        total += check
    print(total)

main()
