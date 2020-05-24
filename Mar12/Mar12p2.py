col = ['ram', 'sham', 'shub', 'khan', 'ravan']
col.sort()
s = 'ram'
fl = 0
low = 0
high = len(col)
m = (low+high)//2

while low <= high:
    m = (low + high) // 2
    if col[m] == s:
        print("Found")
        fl = 1
        break
    elif s > col[m]:
        low = m + 1
    else:
        high =m - 1

if not fl:
    print("Not found")