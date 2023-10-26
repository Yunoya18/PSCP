"""SMS"""
def main():
    """process"""
    num = int(input())
    text = ""
    button_dict = {2 : ["A", "B", "C"], 3 : ["D", "E", "F"], 4 : ["G", "H", "I"],\
                    5 : ["J", "K", "L"], 6 : ["M", "N", "O"], 7 : ["P", "Q", "R", "S"],\
                    8 : ["T", "U", "V"], 9 : ["W", "X", "Y", "Z"]}
    for _ in range(num):
        button = int(input())
        time = int(input())
        if button == 1:
            for _ in range(time):
                text = text[:len(text) - 1]
        elif button == 2 or button == 3 or button == 4 or button == 5\
            or button == 6 or button == 8:
            text += button_dict[button][time%3 - 1]
        elif button == 7 or button == 9:
            text += button_dict[button][time%4 - 1]
    if len(text) == 0:
        text = "null"
    print(text)

main()
