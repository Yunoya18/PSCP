"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """process"""
    text = input()
    text = text.replace(".", " ")
    text_list = text.split()
    vowel = ["a", "e", "i", "o", "u"]
    final_list = []
    for word in text_list:
        count = 0
        for i in word:
            if i in vowel:
                count += 1
        if count >= 2:
            final_list.append(word)
    final_list.sort()
    if len(final_list) == 0:
        print("Nope")
    else:
        print(*final_list, sep="\n")

main()
