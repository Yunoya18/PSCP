"""RockPaperScissor"""
def check(i, text):
    """check side"""
    if text[i] == "R":
        if text[i+1] == "P":
            score = "B"
        elif text[i+1] == "S":
            score = "A"
        else:
            score = "D"
    elif text[i] == "P":
        if text[i+1] == "R":
            score = "A"
        elif text[i+1] == "S":
            score = "B"
        else:
            score = "D"
    elif text[i] == "S":
        if text[i+1] == "P":
            score = "A"
        elif text[i+1] == "R":
            score = "B"
        else:
            score = "D"
    return score

def main():
    """calculate"""
    text = input()
    check_score = ""
    for i in range(0, len(text), 2):
        check_score += check(i, text)
    score_a = check_score.count("A")
    score_b = check_score.count("B")
    if score_a > score_b:
        print("A win", str(score_a) + "-" + str(score_b))
    elif score_b > score_a:
        print("B win", str(score_b) + "-" + str(score_a))
    else:
        print("DRAW", score_a)

main()
