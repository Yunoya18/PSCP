"""Niwarn World"""
import math
def cal_x(num_n):
    """calculate x"""
    num_x = 2 + ((math.log(num_n**2, 2))/(2 * num_n * math.log(num_n, 2)))
    return num_x

def cal_y(num_n, num_s):
    """calculate y"""
    num_y = (math.sin(math.radians(30)) + (2*num_s)**0.5)/((cal_x(num_n)) + 3)
    return num_y

def cal_z(num_k):
    """calculate z"""
    num_z = (cal_y(num_k, num_k))**2 + ((8456 * (cal_x(num_k))**4)/(24*num_k))
    return num_z

def main():
    """process"""
    num_n = float(input())
    num_s = float(input())
    num_k = float(input())
    num_x = cal_x(num_n)
    num_y = cal_y(num_n, num_s)
    num_z = cal_z(num_k)
    print("X: %.1f, Y: %.1f, Z: %.1f" % (num_x, num_y, num_z))

main()
