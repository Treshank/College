import math
c = 0
suma = 0
while True:
    try:
        num = input()
        math.isnan(float(num))
        suma += int(num)
        c += 1
    except ValueError:
        if num == 'done':
            avg = suma/c
            print("sum = ", suma, "\navg=", avg)
            break
        else:
            print("Invalid")
            pass

