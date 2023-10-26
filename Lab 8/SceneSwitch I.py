"""SceneSwitch I"""
def main():
    """proccess"""
    status = True
    daylight = True
    check_time = []
    count = 0
    while True:
        time = input()
        if time == "End":
            break
        check_time.append(float(time))
    for i in range(1, len(check_time)):
        check = check_time[i] - check_time[i-1]
        if status:
            status = False
        else:
            status = True
            if daylight:
                if check <= 6:
                    count += 1
                    daylight = False
            else:
                daylight = True
    print(count)

main()
