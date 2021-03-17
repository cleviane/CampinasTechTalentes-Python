import re

line = "Cats are smarter than dogs"

matchObj = re.watch(r'dogs', line, re.M | re.I)

if matchObj:
   
   print('watch - > watchObj.group() :',watchObj.group())
else:
   print("No watch!!")


