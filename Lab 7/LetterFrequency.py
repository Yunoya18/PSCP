"""LetterFrequency"""
def main():
    """process"""
    text = input()
    count_dict = {}
    for cha in text:
        if cha.isalpha():
            if cha.lower() not in count_dict:
                count_dict[cha.lower()] = text.count(cha.upper()) + text.count(cha.lower())
    sort_countdict = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
    print(sort_countdict[0][0])

main()
