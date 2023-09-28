"""Volleyball"""
def main():
    """calculate"""
    text = input()
    score_a = 0
    score_b = 0
    set_a = 0
    set_b = 0
    for i in text:
        if i == "A":
            score_a += 1
        elif i == "B":
            score_b += 1
        if set_a + set_b == 4:
            if (score_a >= 14 and score_b >= 14 and score_a - score_b == 2)\
                or (score_a == 15 and score_b <= 13):
                print("Set %d: A (%d) | B (%d)" % (set_a + set_b + 1, score_a, score_b))
                set_a += 1
                score_a, score_b = 0, 0
            elif (score_a >= 14 and score_b >= 14 and score_b - score_a == 2)\
                or (score_b == 15 and score_a <= 13):
                print("Set %d: A (%d) | B (%d)" % (set_a + set_b + 1, score_a, score_b))
                set_b += 1
                score_a, score_b = 0, 0
        else:
            if (score_a >= 24 and score_b >= 24 and score_a - score_b == 2)\
                or (score_a == 25 and score_b <= 23):
                print("Set %d: A (%d) | B (%d)" % (set_a + set_b + 1, score_a, score_b))
                set_a += 1
                score_a, score_b = 0, 0
            if (score_a >= 24 and score_b >= 24 and score_b - score_a == 2)\
                or (score_b == 25 and score_a <= 23):
                print("Set %d: A (%d) | B (%d)" % (set_a + set_b + 1, score_a, score_b))
                set_b += 1
                score_a, score_b = 0, 0
    if set_a == 3:
        print("A won %d:%d set" % (set_a, set_b))
    elif set_b == 3:
        print("B won %d:%d set" % (set_b, set_a))
    else:
        print("Set %d: A (%d) | B (%d)" % (set_a + set_b + 1, score_a, score_b))
        print("The game has not finished yet.")

main()
