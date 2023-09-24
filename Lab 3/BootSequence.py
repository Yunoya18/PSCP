"""BootSequence"""
def main():
    """process"""
    num = int(input())
    text = ""
    for i in range(1, num+1):
        text += str(i)
        text += "_"
    print(text[:-1])

main()
