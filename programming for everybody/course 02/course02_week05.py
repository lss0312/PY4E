# dictionaries
# give every element a key and the value
dict1 ={'money':2,'phone':3,'cards':4}
print(dict1['money'])
#>>> 2
dict2 ={}
dict2['money']=1
dict2['apple']=2
dict2['banana']=3
print(dict2)
#>>>{'apple':2,'banana':3,'money':1} dictionaries will not contain the elements in the order you put them in.
# counting with dictionaries
# get()
count=dict()
names=['apple','apple','banana','banana','cards','order']
for name in names:
    count[name] = count.get(name,0)+1 # this can be used to count how many times a certain words appears in the list.
    print(count) 
# >>> {'apple':2,'banana':2,'cards':1,'order':1}
# dictionaries and files
print(list(count))# this will print every key of the dictionary
print(count.keys()) # the same as above
print(value.values()) # this will print every value of the dictionary
print(count.items()) # this will print every pair of the key and value.

fname = input('Enter File: ')
if fname < 1 :
	fname = 'file.txt'
hand = open(fname)
di = dict()
for line in hand:
	line = line.rstrip()
	wds = line.split()
	for w in wds:
		dict[w] = dict.get(w,0)+1
	print(di)
	
# to find the most common words in a dictionary
bigcount = None
bigword = None
for k,v in dic.items():
	if v > bigcount:
		bigcount = v
		bigword = k
	print(k,v)