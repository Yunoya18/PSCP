"""Kabata"""
def main():
    """process"""
    num = int(input())
    for _ in range(num):
        text = input()
        text = text.replace("baka", "!")
        text = text.replace("bakka", "")
        text = text.replace("ka", "")
        text = text.replace("ba", "")
        text = text.replace("ta", "")
        if len(text) == 0:
            print("yes")
        else:
            print("no")

main()
