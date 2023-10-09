"""Muddled Menu"""
def main():
    """process"""
    menu_list = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "SOMETHING'S WRONG":
            menu_list = []
        elif "Can't do: " in menu:
            final_menu = menu.replace("Can't do: ", "")
            menu_list.remove(final_menu)
        elif menu == "CLOSED":
            menu_list = []
            break
        else:
            index = menu.find("#")
            final_menu = menu[:index-1]
            if menu[index+1] == "N":
                menu_list.append(final_menu)
            else:
                menu_list.insert(int(menu[index+1:]) - 1, final_menu)
    print("Full Course:", menu_list, end=" ")
    menu_list.reverse()
    print("Reversed:", menu_list)

main()
