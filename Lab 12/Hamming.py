"""Hamming"""
def main():
    """process"""
    text1 = input()
    text2 = input()
    lenght = 0
    count = 0
    while lenght < len(text1):
        if text1[lenght] != text2[lenght]:
            count += 1
        lenght += 1
    print(count)

main()
