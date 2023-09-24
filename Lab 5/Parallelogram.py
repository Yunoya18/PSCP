"""Parallelogram"""
def main():
    """process"""
    text = input()
    for i in range(len(text)):
        print(" " * (len(text) - i - 1), end="")
        print(text[0:i+1])
    for j in range(1, len(text)):
        print(text[0 + j:len(text)])

main()
