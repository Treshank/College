import re

emails = {}
flag = 0

f = open(input("Enter the name of the file: "), 'r')
for line in f:
    if re.match('From*', line):
        for mail in emails:
            if line.split(' ')[1].rstrip() == mail:
                emails[mail] += 1
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            emails.__setitem__(line.split(' ')[1].rstrip(), 1)

lname = None
lval = None
for mail, val in emails.items():
    if lval is None or val > lval:
        lval = val
        lname = mail

print(lname,':',lval)