import random
import time
input("Please press y to continuie and n to exit")
response="y"
while response=="y":
 no = random.randint(1,6)
 time.sleep(1)
 if no==1:
  print("the number is 1!")
 if no==2:
  print("the number is 2!")
 if no==3:
  print("the number is 3!")
 if no==4:
  print("the number is 4!")
 if no==5:
  print("the number is 5!")
 if no==6:
  print("the number is 6!")
  print("\n")