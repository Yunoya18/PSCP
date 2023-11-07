"""Dancing"""
SIZE_ = int(input())
def check(text, current):
    """check position"""
    if text == "north":
        current = (max(0, current[0]-1), current[1])
    elif text == "northeast":
        current = (max(0, current[0]-1), min(SIZE_-1, current[1]+1))
    elif text == "east":
        current = (current[0], min(SIZE_-1, current[1]+1))
    elif text == "southeast":
        current = (min(SIZE_-1, current[0]+1), min(SIZE_-1, current[1]+1))
    elif text == "south":
        current = (min(SIZE_-1, current[0]+1), current[1])
    elif text == "southwest":
        current = (min(SIZE_-1, current[0]+1), max(0, current[1]-1))
    elif text == "west":
        current = (current[0], max(0, current[1]-1))
    elif text == "northwest":
        current = (max(0, current[0]-1), max(0, current[1]-1))
    return current

def main():
    """process"""
    position = int(input())
    bonus = int(input())
    current = (SIZE_//2, SIZE_//2)
    position = ((position-1)//SIZE_, (position-1) % SIZE_)
    score = 0
    while True:
        text = input().lower()
        if text == "ultimately":
            score += 5*(bonus if current == position else 1)
            break
        elif "dance" in text:
            score += (bonus if current == position else 1)
        else:
            current = check(text, current)
    print("Total point :", score)

main()
