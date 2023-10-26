"""WordSequence II"""
def main():
    """process"""
    text1 = input()
    text2 = input()
    for i in range(max(len(text1), len(text2)) +1):
        print(text2[0:i], end="")
        print(text1[i:])

main()
