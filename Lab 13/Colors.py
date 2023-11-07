"""Colors"""
def main():
    """process"""
    check_color = ["Red", "Yellow", "Blue"]
    color1 = input()
    color2 = input()
    if color1 not in check_color or color2 not in check_color:
        print("Error")
    else:
        if color1 in ["Red", "Blue"] and color2 in ["Red", "Blue"] and color1 != color2:
            print("Violet")
        elif color1 in ["Red", "Yellow"] and color2 in ["Red", "Yellow"] and color1 != color2:
            print("Orange")
        elif color1 in ["Blue", "Yellow"] and color2 in ["Blue", "Yellow"] and color1 != color2:
            print("Green")
        else:
            print(color1)

main()
