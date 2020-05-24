# Write a pyhton fn to find the 1st appearance of the sub string 'not' and 'poor' from a given string. If not followed
# poor, Replace the whole 'not.... poor' with good return the resulting string

def findthis(str):
    p1 = str.find('not')
    p2 = str.find('poor')
    if p1<p2:
        news = str[::p1]
        news += 'good'
        news += str[p2::]
        return news