"""OneTwo"""
def text(num):
    """text"""
    if num == 1:
        return "1"
    elif num == 2:
        return "2"
    final_text = text(num - 1) + text(num - 2)
    return final_text

def main():
    """process"""
    num = int(input())
    print(text(num))

main()
