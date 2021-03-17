# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print("Fofinho, os argumentos não são números queridinho. \n", Argument)


# Call above function here.
temp_convert("xyz")
