"""Password"""
import hashlib
def main():
    """process"""
    text = input().encode("utf-8")
    final_text = hashlib.sha512(text).hexdigest().upper()
    print(final_text)

main()
