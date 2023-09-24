"""Virus I"""
def main():
    """process"""
    text = input()
    total = 0
    for i in text:
        if i == "o":
            total += 1
    print(total)

main()
