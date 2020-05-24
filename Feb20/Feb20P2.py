def smin(a,b,c):
    return a if (a<=b and a<=c) else (b if (b<=a and b<=c) else c)

print(smin(10,4,210))
