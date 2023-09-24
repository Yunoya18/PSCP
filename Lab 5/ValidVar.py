"""ValidVar"""
def main():
    """process"""
    num = int(input())
    reserved = "if else elif while for True False continue\
        break return is in and or from as pass not def None"
    reserved_name = reserved.split(" ")
    for _ in range(num):
        text = input()
        if text.isidentifier():
            if text in reserved_name:
                print("Invalid")
            else:
                print("Valid")
        else:
            print("Invalid")

main()
