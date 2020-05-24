# Reads file and prints in decreasing order of freq

f = open(input("Enter the file name: "))
ini = 0
while True:
    char = f.read(1)
    if not char:
        break
    else:
        fl = 0
        char = char.lower()
        if 'a' <= char <= 'z':
            if ini == 0:
                tup = [(char, 1)]
                ini = 1
            else:
                for t in tup:
                    if t[0] == char:
                        val = t[1] + 1
                        tup.remove((t[0], t[1]))
                        tup.append((char, val))
                        fl = 1
                        break
                if fl == 0:
                    tup.append((char, 1))

tup.sort(key=lambda x: x[1], reverse=1)
for t in tup:
    print(t[0], t[1])
