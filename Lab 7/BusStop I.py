"""BusStop I"""
def main():
    """process"""
    capacity = int(input())
    bus_stop = int(input())
    info = []
    current_bus = []
    count = 0
    for _ in range(bus_stop):
        bus = input().split()
        info.append(bus)
    info.sort(key=lambda i: int(i[0]))
    for i in info:
        stop = int(i[0])
        i = i[1:]
        check_bus = current_bus.copy()
        for arrive in current_bus:
            if arrive == stop:
                check_bus.remove(arrive)
                count += 1
        current_bus = check_bus
        for passenger in i:
            if len(current_bus) < capacity:
                if int(passenger) > stop:
                    current_bus.append(int(passenger))
    print(count)

main()
