"""iPhone 13 Again"""
def mini(storage):
    """iPhone 13 mini"""
    if storage == "128 GB":
        return 25900
    elif storage == "256 GB":
        return 29900
    elif storage == "512 GB":
        return 37900
    else:
        return "Not Available"

def normal(storage):
    """iPhone 13"""
    if storage == "128 GB":
        return 29900
    elif storage == "256 GB":
        return 33900
    elif storage == "512 GB":
        return 41900
    else:
        return "Not Available"

def pro(storage):
    """iPhone 13 Pro"""
    if storage == "128 GB":
        return 38900
    elif storage == "256 GB":
        return 42900
    elif storage == "512 GB":
        return 50900
    elif storage == "1 TB":
        return 58900
    else:
        return "Not Available"

def pro_max(storage):
    """iPhone 13 Pro Max"""
    if storage == "128 GB":
        return 42900
    elif storage == "256 GB":
        return 46900
    elif storage == "512 GB":
        return 54900
    elif storage == "1 TB":
        return 62900
    else:
        return "Not Available"

def main():
    """process"""
    name = input()
    storage = input()
    if name == "iPhone 13 mini":
        print(mini(storage))
    elif name == "iPhone 13":
        print(normal(storage))
    elif name == "iPhone 13 Pro":
        print(pro(storage))
    elif name == "iPhone 13 Pro Max":
        print(pro_max(storage))
    else:
        print("Not Available")

main()
