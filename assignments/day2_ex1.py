list = input("Enter list of ele separated by comma: ").split(',')
n = int(input("Enter the size to sort: "))
for e in list:
    if len(e) > n-1:
        print(e)