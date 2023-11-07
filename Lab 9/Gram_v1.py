"""Gram_v1"""
def main():
    """process"""
    text = input()
    word = {}
    word_total = []
    while len(text) > 1:
        word[text[0:2]] = word.get(text[0:2], 0) + 1
        word_total.append(text[0:2])
        text = text[1:]
    count_list = list(word.values())
    word_list = list(word)
    highest = max(count_list)
    highest_word = word_list[count_list.index(highest)]
    print(highest_word, highest, sep="\n")

main()
