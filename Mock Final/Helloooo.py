"""Helloooo"""
def main():
    """process"""
    text = input()
    final_text = ""
    count = 0
    for cha in reversed(text):
        if cha in ["a", "e", "i", "o", "u"] and count == 0:
            final_text += (cha * 4)
            count += 1
        else:
            final_text += cha
    final_text = final_text[::-1]
    print(final_text)

main()
