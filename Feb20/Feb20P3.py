def grade_comp(sc):
    if sc > 0.9 :
        return 'A'
    elif sc > 0.8:
        return 'B'
    elif sc > 0.7:
        return 'C'
    elif sc > 0.6:
        return 'D'
    else:
        return 'E'


if __name__ == '__main__':
    print(grade_comp(0.99))
    print(grade_comp(0.89))
    print(grade_comp(0.79))
    print(grade_comp(0.69))
    print(grade_comp(0.59))
    print(grade_comp(0.49))

