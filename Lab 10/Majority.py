"""Majority"""
def main():
    """process"""
    int(input())
    score = {}
    voter = int(input())
    for _ in range(voter):
        vote = int(int(input()))
        score[vote] = score.get(vote, 0) + 1
    score_list = list(score.values())
    highest = max(score_list)
    if highest <= voter / 2:
        print(0, highest)
    else:
        number = list(score)[score_list.index(highest)]
        print(number, highest)

main()
