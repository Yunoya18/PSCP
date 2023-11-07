"""Socks"""
def main():
    """process"""
    sock = {}
    text = input()
    total = 0
    for cha in text:
        sock[cha] = sock.get(cha, 0) + 1
    sock = dict(sorted(sock.items()))
    sock_pair = []
    for item, num in sock.items():
        for _ in range(num//2):
            sock_pair.append(item*2)
        total += num//2
    if len(sock_pair) == 0:
        print("None")
    else:
        print(*sock_pair, sep=" ")
    print(total)

main()
