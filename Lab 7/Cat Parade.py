"""Cat Parade"""
def main():
    """process"""
    cat_name = []
    print_list = []
    while True:
        cat = input()
        if cat == "IT'S A DOG":
            cat_name.remove(cat_name[-1])
        elif "," in cat:
            another_cat = cat.split(", ")
            cat_name.extend(another_cat)
        elif cat == "END":
            break
        else:
            cat_name.append(cat)
    sort_catname = sorted(cat_name)
    for i in sort_catname:
        if i not in print_list:
            position = cat_name.index(i) + 1
            count = cat_name.count(i)
            print(i, position, count)
            print_list.append(i)

main()
