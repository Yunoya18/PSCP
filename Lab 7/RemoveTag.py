"""RemoveTag"""
def main():
    """process"""
    text = input()
    check = False
    word = ""
    word_list = []
    index = text.find("<")
    if index == -1:
        word_list = text.split()
    else:
        for i in text:
            if check:
                if i == "<":
                    if word != "":
                        word = word.strip()
                        word_list.extend(word.split())
                        word = ""
                    check = False
                else:
                    word += i
            else:
                if i == ">":
                    check = True
    print(word_list)

main()
