while True:
    str=input()
    if str.lower() == 'done':
        break
    elif str.startswith('#'):
        continue
    else:
        print(str)