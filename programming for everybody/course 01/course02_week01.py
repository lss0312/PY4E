# course 02_week01
# string
#1. string can be printed
print('hello')
#2. string can not be added to an int, you should use int function to change it into an int
num = int('123') + 1
print(num)
#3. the function of input will return a string
num2 = input('number: ')
print(type(num2)) 
#4. string can be a kind of list
string1 = 'banana'
print(string1[2])
#5. string has a lenth which can be used to form a loop
print(len(string1))
word='banana'
for i in word:
  print(i)
#6. slicing string: using the [a:b]
# a means begin with, b means end but not included.
word2='apple'
print(word2[:2])
print(word2[1:2])
print(word2[:])
#7. str.****() can be used for varis purposes.
print('banana'.capitalize()) # change the first letter into uppercase, but other letter into lowercase.
print('banana'.find('a')) # return the position that python first find the 'a' in the string
print('banna'.find('1'))#if python can not find any, it will return -1.
print('banana'.replace('a','b'))#method replace can be used to replace the old letter with the new one, you need put two words to be used in this method.
# execise 6.5
str = 'X-DSPAM-Confidence: 0.8475'
start=str.find(':')
print(float(str[start+1:]))
# strip means to remove the useless whitespace, rstrip will remove the whitespace on the right of the words, lstrip will remove those on the left.
print(strip('     hello world    '))
#>>> it will print hello world.

