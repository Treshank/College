ini = 0
f = open(input("Enter the file name: "))
for line in f:
    fl = 0
    l = line.split(' ')
    if l[0] == "From":
        try:
            time = l[6].rstrip()
            hr = str(time.split(':')[0])
            if ini == 0:
                tup = [(hr, 1)]
                ini = 1
            else:
                for t in tup:
                    if t[0] == hr:
                        val = t[1] + 1
                        tup.remove((t[0], t[1]))
                        tup.append((hr, val))
                        fl = 1
                        break
                if fl == 0:
                    tup.append((hr, 1))
        except:
            pass
for t in tup:
    print(t[0], t[1])
