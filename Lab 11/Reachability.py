"""Reachability"""
import json
PATH_ = set()
NODE_ = json.loads(input().replace("'", "\""))
def check(start):
    """check"""
    path_check = NODE_[start]
    if len(path_check) > 0:
        for i in path_check:
            if i not in PATH_:
                PATH_.add(i)
                check(i)

def main():
    """process"""
    start = input()
    check(start)
    PATH_.add(start)
    path = list(PATH_)
    path.sort()
    print(path)

main()
