# tuples
t = (a,b,c)
print(t[2]) # tuples are like lists
#>>> c
# tuples are not mutable
# tuples can not be sorted and appended
#tuples are usually used to memory a temporay varibles.
c = {'a':1,'c':22,'b':20}

tmp = c.items(c) # this give a list of tuples
#>>> tmp = [(a,1),(c,22),(b,20)]
print(sorted(tmp)) # sort by the key.
#>>> [(a,1),(b,20),(c,22)]

(0,1,2) < (5,1,2) # tuples can be compared, it will compare the first element if it is the same,then the second one, otherwise, it will get the conclusion.
#>>>true 

#exercise
