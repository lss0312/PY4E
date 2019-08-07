#list
# list is a colletion, which we can put many variables in a list
print([1,2,3])#what list is like
print([])#list can be empty
print([1,[2,3],3]) # list element can be any object in python, even a list.
print(['123','good',1,2])# elements in the same list can be different types.
friends =['a','b','c']
for friend in friends:
	print('hello',friend)# use list to form a loop
print(friends[2])# used to find a element in certain position.
# >>> c
friends[1]='fine'
print(friends)# elements in a list can be replaced by a new object. string does not have this kind of attribute.
#>>>['a','fine','c']
print(len(friends))# len of a list means the number of elements in a list.
#>>> 3
print(range(friends)) # function range will return a list 
#>>> [0,1,2]
print(range(4))
#>>>[0,1,2,3]
# range function can be used to form a counted loop
friends=['a','b','c']
for friend in friends:
    print('hello', friend)

# lists can be added
list1 = [1,2,3,4,5]
list2 = [10,6,8,7]
print(list1 + list2)
#>>> [1,2,3,4,5,10,6,8,7] 
# slice
print(list1[:2])
#>>> [1,2]
# append()
list1.append('10')
print(list1)
#>>>[1,2,3,4,5,'10'] # append()function can be used to add new element into a list, but they can only be added to the end of the list. which means that if you keep append several elements, they will be set in the list in the order you put them in.
# sort() can be used to order list itself
list2.sort()
print(list2)
#>>>[6,7,8,10]
# max 
# mix
# mean
# sum

# list and strings
# split() can be used to form a list of a strings, which every word in the string will be an element.
words = 'hello my friends'
print(words.split())
#>>> ['hello','my','friends']
words2 = 'hello;my;friend'
print(words2.split())
#>>>['hello;my;friend'] #slip is default to split the string by the space between two elements, if you want to split the string by something else, say ';', you should tell the function by put ';' into it
print(words2.split(';'))
#>>>['hello','my','friend']

### exercise ### 
han = open('file')
for line in han:
	line=line.rstrip()
	wds = line.split()
	if len(wds) < 3 or if wds[0] != 'From':#guardian comes first!
		continue
    print(wds[2])