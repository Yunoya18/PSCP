"""Phasmophobia"""
def main():
    """process"""
    ghost = set(["Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", "Poltergeist",\
                 "Revenant", "Shade", "Spirit", "Wraith", "Yurei"])
    for _ in range(3):
        evi = input()
        if evi == "No evidence":
            pass
        else:
            if evi == "EMF Level 5":
                ghost_check = set(["Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"])
            elif evi == "Ghost Writing":
                ghost_check = set(["Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"])
            elif evi == "Fingerprints":
                ghost_check = set(["Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"])
            elif evi == "Spirit Box":
                ghost_check = set(["Demon", "Jinn", "Mare", "Oni", "Poltergeist",\
                                   "Spirit", "Wraith"])
            elif evi == "Freezing Temperatures":
                ghost_check = set(["Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"])
            elif evi == "Ghost Orb":
                ghost_check = set(["Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"])
            ghost = ghost.intersection(ghost_check)
    ghost_list = list(ghost)
    if len(ghost_list) == 0:
        print("Not yet discovered")
    else:
        ghost_list.sort()
        print(*ghost_list, sep="\n")

main()
