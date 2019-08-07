# file
# function: open() to open a file
# read() to read the whole file, but not print it 
fhand = open('file.txt')
inp = fhand.read()#save the file into a string
print(len(inp))
# python will count every characters in the file.txt, not the lines
# \n means new line, it represent one character
sen = 'a\nb'
print(len(sen))
# >>> 3
# find some certain things in a file
#1. .startwith()
print(line.startwith('good'))# print every line that start with 'good'
if 'good' in lines:
print(lines)# print every line that contains the word 'good'
# exercise 7.1: read a file and print the content all in upper case
fh = open('')
print(upper(fh)) #print the name and other info of the file,but not the content line by line.
for lx in fh:
	ly = lx.rstrip()
	print(ly.upper（）)# print every line in the file. and remove the useless whitespaces.
