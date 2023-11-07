"""BreakPassword"""
import hashlib
def main():
    """calculate"""
    text = input()
    for i in range(100000):
        i = "%05d" % i
        check_text = str(i).encode("utf-8")
        check_text = hashlib.sha512(check_text).hexdigest().upper()
        if check_text == text:
            print(i)
            break

main()
