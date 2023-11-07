"""iPad Air"""
def main():
    """process"""
    color = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    need_color = input()
    capa = int(input())
    connect = input()
    if need_color in color:
        if connect == "Wi-Fi":
            if capa == 64:
                print(19900)
            elif capa == 256:
                print(24900)
            else:
                print("Not Available")
        elif connect == "Wi-Fi + Cellular":
            if capa == 64:
                print(24400)
            elif capa == 256:
                print(29400)
            else:
                print("Not Available")
        else:
            print("Not Available")
    else:
        print("Not Available")

main()
