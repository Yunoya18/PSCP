"""Impostor"""
import json
def main():
    """process"""
    character_dict = {}
    dead_cha = {}
    count = 0
    while True:
        text = input()
        if text == "Start":
            break
        else:
            character = json.loads(text)
            character_dict.update(character)
    while True:
        del_cha = input()
        if del_cha == "End":
            break
        dead_cha[del_cha] = character_dict.pop(del_cha)
    for i in character_dict.values():
        if i == "Impostor":
            count += 1
    character_dict = dict(sorted(character_dict.items()))
    dead_cha = dict(sorted(dead_cha.items()))
    print("%d Impostor Remains" % count)
    print("***Alive***")
    for cha in character_dict:
        print("%s : %s" % (cha, character_dict[cha]))
    print("***Dead***")
    for dead in dead_cha:
        print("%s : %s" % (dead, dead_cha[dead]))

main()
