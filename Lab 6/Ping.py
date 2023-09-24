"""Ping"""
def check_recive(line1, line2, line3, line4):
    """check recive"""
    recive = 0
    if "Reply" in line1:
        recive += 1
    if "Reply" in line2:
        recive += 1
    if "Reply" in line3:
        recive += 1
    if "Reply" in line4:
        recive += 1
    return recive

def check_time(line):
    """check time"""
    time_index = line.find("time=")
    end_index = line.find("ms")
    if time_index == -1:
        time = 0
    else:
        time = int(line[time_index+5:end_index])
    return time

def check_min(minimum, line1, line2, line3, line4):
    """check min"""
    minimum = 0
    if line1.find("time=") != -1:
        time_index = line1.find("time=")
        end_index = line1.find("ms")
        minimum = int(line1[time_index+5:end_index])
    if line2.find("time=") != -1:
        time_index = line2.find("time=")
        end_index = line2.find("ms")
        if minimum == 0:
            minimum = int(line2[time_index+5:end_index])
        else:
            minimum = min(minimum, int(line2[time_index+5:end_index]))
    if line3.find("time=") != -1:
        time_index = line3.find("time=")
        end_index = line3.find("ms")
        if minimum == 0:
            minimum = int(line3[time_index+5:end_index])
        else:
            minimum = min(minimum, int(line3[time_index+5:end_index]))
    if line4.find("time=") != -1:
        time_index = line4.find("time=")
        end_index = line4.find("ms")
        if minimum == 0:
            minimum = int(line4[time_index+5:end_index])
        else:
            minimum = min(minimum, int(line4[time_index+5:end_index]))
    return minimum

def main():
    """process"""
    input()
    input()
    line1 = input()
    line2 = input()
    line3 = input()
    line4 = input()
    line5 = input()
    ip_index = line1.find("[")
    if ip_index == -1:
        start_index = line1.find("Pinging") + 8
        end_index = line1.find(" with")
        ip_address = line1[start_index:end_index]
    else:
        ip_address = line1[line1.find("[")+1:line1.find("]")]
    recive = check_recive(line2, line3, line4, line5)
    print("Ping statistics for", ip_address + ":")
    print("    Packets: Sent = 4, Received = %d, Lost = %d (%d%% loss),"\
          % (recive, (4-recive), (((4-recive)/4)*100)))
    if recive != 0:
        minimum = check_min(0, line2, line3, line4, line5)
        maximum = max(check_time(line2), check_time(line3), check_time(line4), check_time(line5))
        average = (check_time(line2) + check_time(line3) + check_time(line4) + check_time(line5))\
            // recive
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" % (minimum, maximum, average))

main()
