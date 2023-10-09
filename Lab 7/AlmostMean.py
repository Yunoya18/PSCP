"""AlmostMean"""
def main():
    """process"""
    num = int(input())
    code_list = []
    score_list = []
    final_score = 0
    for _ in range(num):
        text = input()
        text_list = text.split("\t")
        code_list.append(text_list[0])
        score_list.append(float(text_list[1]))
    mean = sum(score_list) / num
    for i in score_list:
        if i < mean and i > final_score:
            final_score = i
    position = score_list.index(final_score)
    print(code_list[position] + "\t" + str(final_score))

main()
