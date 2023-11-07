"""WPM"""
def check_kid(wpm):
    """check range"""
    if wpm < 11:
        print("Very Slow")
    elif 11 <= wpm <= 20:
        print("Slow")
    elif 21 <= wpm <= 30:
        print("Average")
    elif 31 <= wpm <= 40:
        print("Fast")
    else:
        print("Very Fast")

def check_adult(wpm):
    """check range"""
    if wpm < 26:
        print("Very Slow")
    elif 26 <= wpm <= 35:
        print("Slow/Beginner")
    elif 36 <= wpm <= 45:
        print("Intermediate/Average")
    elif 46 <= wpm <= 65:
        print("Fast/Advanced")
    elif 66 <= wpm <= 80:
        print("Very Fast")
    else:
        print("Insane")

def main():
    """process"""
    age = input()
    wpm = int(input())
    if age == "Kids":
        check_kid(wpm)
    else:
        check_adult(wpm)

main()
