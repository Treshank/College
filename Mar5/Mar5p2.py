# define a function to get a string made of the first 2 and last 2 char from a given string
# if the string length is less than 2, return empty string

def MakeString(s1, s2):
    sl1 = slice(0, 2, 1)
    sl2 = slice(len(s2)-2, len(s2), 1)
    news = s1[sl1]+s2[sl2]
    if(len(news)<2):
        return ''
    return news

print("op= ",MakeString('m',''))