# define a fn to get a string from the given string where all occurances of its first char has been changed to '$'
# except the first char itself

def replacer(s):
    fs=s[0]
    for i in range(1, len(s)):
        if s[i] == fs[0]:
            fs += '$'
        else:
            fs += s[i]
    return fs


print(replacer('hello hi how are you doingh'))