"""CompositeFunction"""
def func_f(num):
    """function f"""
    total = 2 * num
    return total

def func_g(num):
    """function g"""
    total = num / 2 + 1
    return total

def main():
    """process"""
    num = int(input())
    print("%.2f" % func_f(func_g(num)))
    print("%.2f" % func_g(func_f(num)))

main()
