"""Filter"""
import json
def main():
    """process"""
    text = input()
    num = float(input())
    score_list = json.loads(text)
    final_list = {}
    for key, value in score_list.items():
        if value >= num:
            final_list[key] = value
    if len(final_list) == 0:
        print("Nope")
    else:
        final_list = dict(sorted(final_list.items()))
        for new_key, new_value in final_list.items():
            print("%s\t%.2f" % (new_key, float(new_value)))

main()
