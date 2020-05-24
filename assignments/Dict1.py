# Read parse from pull out address and count the no of email in that day of week.

import re

days = {
    'Mon': 0,
    'Tue': 0,
    'Wed': 0,
    'Thur': 0,
    'Fri': 0,
    'Sat': 0,
    'Sun': 0
}

f = open(input("Enter the name of the file: "), 'r')
for line in f:
    if re.match('From*', line):
        try:
            for item in days:
                if line.split(' ')[2] == item:
                    days[item] += 1
                    break
        except IndexError:
            pass

for item, val in days.items():
    if val != 0:
        print(item, ':', val)
