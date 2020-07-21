import sys

def calculate():
	print("------------------------Welcome to Faulty Calculator----------------------")
	a=int(input("Enter the value of a:\n"))
	b=int(input("Enter the value of b:\n"))
	operator = int(input("\npress 1 for +\n press 2 for -\n press 3 for *\n press 4 for //\n Enter the operator\n"))
	if a==56 and b==7 and operator == 1 :
	    print("Wrong answer:",77)
	elif operator == 1:
	    print("The plus of two no:",a+b)
	elif operator == 2:
	    print("The difference of two no:",a-b)
	elif a==45 and b==3 and operator == 3:
	    print("Wrong answer:",190)
	elif operator == 3:
	    print("The mult of two no:",a*b)
	elif a==56 and b==6 and operator == 4:
	    print("Wrong answer:",4)
	elif operator == 4:
	    print("The divion of two no ==:",a//b)   
	else:
	    print("Invalid operator")
		
	selection = int(input("\npress 1 for Calculate again\n press 2 for Exit\n"))
	return selection

def runCalculate(inp):
	if(inp == 1):
		choice = calculate()
		runCalculate(choice)
	elif(inp == 2):
		sys.exit()
		
print("------------------------Welcome to Module----------------------")

runCalculate(1)


