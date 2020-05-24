#Count no of messages from each person.
ini = 0
f = open(input("Enter the file name: "))
for line in f:
    fl = 0
    l = line.split(' ')
    if l[0] == "From":
        mail = l[1].rstrip()
        if ini == 0:
            tup = [(mail, 1)]
            ini = 1
        for t in tup:
            if t[0] == mail:
                val = t[1] + 1
                tup.remove((t[0], t[1]))
                tup.append((mail, val))
                fl = 1
                break
        if fl == 0:
            tup.append((mail, 1))

for t in tup:
    print(t[0], t[1])
