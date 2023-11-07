"""Fever"""
def main():
    """process"""
    temp = float(input())
    if temp < 38:
        print("No Fever")
    elif temp < 39:
        print("Mild Fever")
    elif temp < 40:
        print("High Fever")
    else:
        print("Very High Fever")

main()
