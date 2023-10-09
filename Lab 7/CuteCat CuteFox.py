"""CuteCat CuteFox"""
def change(text):
    """change"""
    final_text = []
    text = text.replace("{", "").replace("}", "")
    text_list = text.split(":")
    for i in text_list:
        final_text.append(i.strip().strip('"').strip("'"))
    return final_text

def main():
    """process"""
    num = int(input())
    animal = {}
    cat_count = 0
    fox_count = 0
    for _ in range(num):
        animal_input = change(input())
        animal[animal_input[1]] = animal_input[0]
    if "Garfield" not in list(animal.values()) and "Cat01" not in list(animal.keys()):
        animal.update({"Cat01" : "Garfield"})
    if "Fubuki" not in list(animal.values()) and "Fox01" not in list(animal.keys()):
        animal.update({"Fox01" : "Fubuki"})
    animal = dict(sorted(animal.items(), key=lambda x: (x[0][:3], int(x[0][3:]))))
    for count in animal.keys():
        if "Cat" in count:
            cat_count += 1
        elif "Fox" in count:
            fox_count += 1
    print("Cat :", cat_count)
    print("Fox :", fox_count)
    for key, value in animal.items():
        print(value, ":", key)

main()
