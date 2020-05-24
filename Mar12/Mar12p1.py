s = input("Enter a sentence: ")
sls = s.split(" ")
print("The words and lengths are..")
for i in sls:
    print(i, len(i))