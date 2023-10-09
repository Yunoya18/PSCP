"""LastStand"""
import json
def main():
    """process"""
    num = json.loads(input())
    for i in num:
        print(str(i)[-1])

main()
