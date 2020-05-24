import re

emails = {}
flag = 0

f = open(input("Enter the name of the file: "), 'r')
for line in f:
    if re.match('From*', line):
        word = line.split(' ')[1].rstrip()
        for mail in emails:
            if word.split('@')[1] == mail:
                emails[mail] += 1
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            emails.__setitem__(word.split('@')[1], 1)

for mail, count in emails.items():
    print(mail, ':', count)

