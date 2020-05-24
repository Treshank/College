l = []
l = list(map(int, input("Enter list ").split(',')))
min=l[0]
for i in l:
    if i<min:
        min=i

print(min)