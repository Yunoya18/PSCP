"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def main():
    """process"""
    name = input()
    if name == "BULL SHARK":
        print("THE SHALLOW ZONE")
    elif name in ["CHAIN CATSHARK", "GREAT WHITE SHARK", "GUMMY SHARK", "BLUE SHARK", "MAKO SHARK"]:
        print("THE TWILIGHT ZONE")
    elif name in ["FRILLED SHARK", "GOBLIN SHARK", "SIXGILL SHARK", "GREENLAND SHARK",\
                  "COOKIECUTTER SHARK"]:
        print("THE MIDNIGHT ZONE")
    elif name == "MEGAMOUTH SHARK":
        print("THE ABYSSAL ZONE")
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")

main()
