# WAPython function to get a single string from 2 given strings separated by a space and swap the 1st 2 char of each
# string

def sep(s):
    new1, new2 = s.split(' ')
    new1c = new2[0]
    new1c += new1[1::]
    new2c = new1[0]
    new2c += new2[1::]
    print(new1c, '\n', new2c)

sep('hello darkness')