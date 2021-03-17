def functionName(level):
   if level < 1:
      raise Exception(level, "xiiiiiiii")
      # The code below to this would not be executed
      # if we raise the exception
   return level


try:
   l = functionName(-10)
   print("level = ", l)
except Exception as e:
   print("Fofinho, deu erro... Olha o valor...", e.args[0], e.args[1])
