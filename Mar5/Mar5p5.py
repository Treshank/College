# Write a python fn to add 'ing' at the end of the given string if the len of the string is at least 3
# If the given string already ends with 'ing' then add 'ly' instead. If string length<3 leave it unchanged

def ing(s):
    if len(s) < 3:
        return s
    elif s[len(s)-3::] == 'ing':
        s += 'ly'
    else:
        s += 'ing'
    return s

print(ing('adding'))