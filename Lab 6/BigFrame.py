"""BigFrame"""
def main():
    """process"""
    string1 = input().strip()
    string2 = input().strip()
    string3 = input().strip()
    string4 = input().strip()
    string5 = input().strip()
    width = max(len(string1), len(string2), len(string3), len(string4), len(string5))
    print("*" * (width + 4))
    print("*", string1 + " " * (width - len(string1)), "*")
    print("*", string2 + " " * (width - len(string2)), "*")
    print("*", string3 + " " * (width - len(string3)), "*")
    print("*", string4 + " " * (width - len(string4)), "*")
    print("*", string5 + " " * (width - len(string5)), "*")
    print("*" * (width + 4))

main()
