from time import sleep
c = 0
for c in range(1, 51):
   sleep (0.2)
   par = (c % 2)
   if par == 0:
      print(c)
      c = c + 1
   else:
      c = c + 1
      