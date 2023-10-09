"""BreachTheDoor"""
def main():
    """process"""
    text = input()
    text_list = text.split()
    final_list = []
    for i in text_list:
        check = ""
        for cha in i:
            if cha.isalpha():
                check += cha
        if len(check) > 6:
            final_list.append(check)
    print(*final_list)

main()
