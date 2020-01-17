#from collections import Counter
#c = Counter('Hello')
#print(c)


str1 = 'ehfdsfasdl'
str2 = 'hell'


def scramble(str1, str2):
    """Returns true if a portion of str1 characters can be rearranged to match str2,
    otherwise returns false."""
    d = {i:str2.count(i) for i in str2}
    d2 = {i:str1.count(i) for i in str1 if i in d}
    return len(d2) == len(d)


print(scramble(str1, str2))
