"""RectangleArea"""
def main():
    """process"""
    rec_ax, rec_ay, width_a, height_a = (int(i) for i in input().split())
    rec_bx, rec_by, width_b, height_b = (int(i) for i in input().split())
    toprec_ax, toprec_ay = rec_ax + width_a, rec_ay + height_a
    toprec_bx, toprec_by = rec_bx + width_b, rec_by + height_b
    if toprec_ax >= rec_bx and toprec_ay >= rec_by:
        width = min(toprec_ax, toprec_bx) - max(rec_ax, rec_bx)
        height = min(toprec_ay, toprec_by) - max(rec_ay, rec_by)
        print(int(width * height))
    else:
        print("no overlapping")

main()
