"""Pad Thai"""
def main():
    """process"""
    ingredient = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",\
                  "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    text = ""
    check_ingre = []
    taste = []
    while True:
        check = input()
        if check == "Cook":
            break
        if check not in ingredient:
            text = "This is not Pad Thai!!!"
        else:
            if check not in check_ingre:
                check_ingre.append(check)
    while True:
        check = input()
        if check == "End":
            break
        if check not in taste:
            taste.append(check)
    if text == "":
        if check_ingre != ingredient:
            text = "This is bad!"
        else:
            if taste != ["Sweet", "Sour", "Salty"]:
                text = "Not Bad..."
            else:
                text = "Delicious!"
    print(text)

main()
