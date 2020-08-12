n=18
guess=1
while guess<10:
  number=int(input("Enter your number:\n"))
  if(number<n):
      print("Your number is smaller than the number")
  elif(number>n):
      print("Your number is greater than the number")
  else:
      print("YOUR GUESS is right it is 18 you took guess= ",guess)
      break
  guess+=1
  if guess==10:
      print("GAME OVER!!!!")