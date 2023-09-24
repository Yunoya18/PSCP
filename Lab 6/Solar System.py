"""Solar System"""
def check_sun(check_text, count):
    """check index sun"""
    while True:
        index = check_text.find(" ")
        if index == -1:
            break
        check = check_text[:index]
        if check == "Sun":
            index_sun = count
        count += 1
        check_text = check_text[index + 1:]
    return index_sun

def main():
    """process"""
    text = input() + " "
    count = 1
    check_text = text
    cold_index = 0
    hot_index = 0
    cold = ""
    hot = ""
    index_sun = check_sun(check_text, count)
    while True:
        planet_index = text.find(" ")
        if planet_index == -1:
            break
        planet_check = text[:planet_index]
        if planet_check != "Sun":
            if cold_index == 0 and hot_index == 0:
                cold = planet_check + " "
                hot = planet_check + " "
                cold_index = abs(count - index_sun)
                hot_index = abs(count - index_sun)
            else:
                if abs(count - index_sun) > cold_index:
                    cold_index = abs(count - index_sun)
                    cold = planet_check + " "
                elif abs(count - index_sun) == cold_index:
                    cold += planet_check + " "
                if abs(count - index_sun) < hot_index:
                    hot_index = abs(count - index_sun)
                    hot = planet_check + " "
                elif abs(count - index_sun) == hot_index:
                    hot += planet_check + " "
        text = text[planet_index+1:]
        count += 1
    print("Hot:", hot.strip())
    print("Cool:", cold.strip())

main()
