import re

f = open(input("Enter the file name: "))
n = 0
nos = 0
for line in f:
    for i in re.findall(r'\d+',line):
        nos += int(i)
        n += 1

avg = int(nos/n)
print(avg)
