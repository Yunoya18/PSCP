"""Palindrome"""
def check_time(hour, small_value):
    """check time"""
    if int(small_value[0]) >= 6:
        hour = str(int(hour) + 1)
        small_value = hour[::-1]
    if hour == "24":
        hour = "0"
        small_value = hour[::-1]
    if int(small_value) >= 60:
        hour, small_value = check_time(hour, small_value)
    return hour, small_value

def main():
    """process"""
    num = int(input())
    time = input()
    count = 1
    index = time.find(":")
    hour = time[:index]
    small_value = time[index+1:]
    if hour == small_value[-1]:
        small_value = str(int(small_value) + 10)
    elif hour == small_value[::-1]:
        hour = str(int(hour) + 1)
    while count <= num:
        if len(hour) == 1:
            if int(hour) < int(small_value[-1]):
                small_value = str(int(small_value) + 10)
            small_value = small_value[0] + hour
        elif len(hour) == 2:
            if int(small_value) > int(hour[::-1]):
                hour = str(int(hour) + 1)
            small_value = hour[::-1]
        hour, small_value = check_time(hour, small_value)
        check = "%d%02d" % (int(hour), int(small_value))
        if check == check[::-1]:
            time = "%d:%02d" % (int(hour), int(small_value))
            print(time)
            count += 1
        if len(hour) == 1:
            small_value = str(int(small_value) + 10)
        elif len(hour) == 2:
            hour = str(int(hour) + 1)

main()
