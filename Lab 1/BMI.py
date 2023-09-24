"""BMI"""
def cal_bmi(name, weight, tall):
    """calculate"""
    bmi = weight / ((tall / 100)**2)
    print(name + "'s  BMI = %.2f" % bmi)

cal_bmi(input(), float(input()), float(input()))
cal_bmi(input(), float(input()), float(input()))
cal_bmi(input(), float(input()), float(input()))
cal_bmi(input(), float(input()), float(input()))
cal_bmi(input(), float(input()), float(input()))
