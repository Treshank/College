f = open('romeo.txt', 'r')
list = []
fl=0
for line in f:
    lineee = line.split('\n')
    words = lineee[0].split(' ')
    for word in words:
        for l in list:
            if l == word.lower():
                fl = 1
                break
        if fl == 0:
            list.append(word.lower())
        else:
            fl = 0
list.sort()
print(list)