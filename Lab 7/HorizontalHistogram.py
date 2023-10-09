"""HorizontalHistogram"""
def check(text):
    """sort"""
    if text.islower():
        return ord(text)
    else:
        return ord(text) + 58 #ให้เกินค่าของ z

def main():
    """process"""
    text = input()
    count_word = {}
    final_word = {}
    for cha in text:
        if cha not in count_word:
            count_word[cha] = text.count(cha)
    count_list = list(count_word)
    count_list.sort(key=check)
    for i in count_list:
        his = ""
        lenght = count_word[i]
        for j in range(lenght):
            if j % 5 == 0:
                his += "|"
            his += "-"
        final_word[i] = his.lstrip("|")
    for word in final_word:
        print(word, ":", final_word[word])

main()
