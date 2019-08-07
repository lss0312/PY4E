# regular expressions
# means some functioning expression
import re # means in this py file we can use regular expressions.
# regular expressions are powerful when we want to find some certain lines in a file.
^word #something begin with'word' 
x = From: now ha ha : oh~
.findall('^From +:') # get all that matches ,and return the bigest line that match
#>>> From: now ha ha :
.findall('from: +?',x) #？tell the py that to get the shortest one that matches.
#>>> From:
# do not use regular expressions to confuss your readers and remember to make comments on your code.