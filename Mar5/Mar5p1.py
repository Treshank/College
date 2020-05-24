# Take the following python code that stores a string str='X-DSPAM-Confidencec:0.8475 use find and string slicing to
# extract the portion of the string after the colon char and then use the float fn to convert extracted string into a
# floating point no

str = 'X-DSPAM-Confidencec:0.8475'
p = str.find(':')
s = slice(p+1, len(str), 1)
print(str[s])


