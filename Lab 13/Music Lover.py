"""Music Lover"""
def main():
    """process"""
    num = int(input())
    song_dct = {}
    for _ in range(num):
        song = input().strip().split("-")
        if song_dct.get(song[0], 0) == 0:
            song_dct[song[0]] = [song[1]]
        else:
            song_dct[song[0]].append(song[1])
    for key, value in song_dct.items():
        print(key)
        print(*value, sep="\n")

main()
