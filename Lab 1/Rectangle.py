"""Rectangle"""
def cal_area(height, width):
    """calculate"""
    area = width * height
    return area

def cal_lenght(height, width):
    """calculate"""
    lenght = (height + width) * 2
    return lenght

def main():
    """calculate"""
    height = int(input())
    width = int(input())
    area = cal_area(height, width)
    lenght = cal_lenght(height, width)
    print(area)
    print(lenght)

main()
