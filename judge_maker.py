def make_judge(grade, points):
    #3回以上３０点以下の成績をとっているか
    is_retest=
    #１回でも１０点より下の点数をとっているか
    is_out=
    if is_out:
        return 3
    elif is_retest:
        return 2
    elif grade=="A"or grade=="B"or grade=="C":
        return 1
    elif grade == "D":
        return 2
