import re

line = "Cats are smarter than dogs"
# match so no começo
matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:

   print('match - > matchObj.group() :', matchObj.group())
else:
   print("No match!!")
# search vai em qualquer lugar da string
searchObj = re.search(r'dogs', line, re.M | re.I)
if searchObj:
   print('searchObj - > searchObj.group() :', searchObj.group())

else:
   print("Nothing found!!")
