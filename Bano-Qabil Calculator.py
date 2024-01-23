#BANO-QABIL CALCULATOR

#declaring required variables
num1 = 0
num2 = 0
result = 0
operator = 0

#getting operator from user
#giving instructions
print("   || INSTRUCTIONS ||   ")
print(" Press 1 for ADDITION")
print(" Press 2 for SUBTRACTION")
print(" Press 3 for MULTIPLICATION")
print(" Press 4 for DIVISION")
print("")

#gettting input
operator = int(input("Enter Operator Number From Instructions: "))
print("")
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

#performing calculations based on input
if operator == 1:
    result = num1 + num2
elif operator == 2:
    result = num1 - num2
elif operator == 3:
    result = num1 * num2
elif operator == 4:
    result = num1 / num2
    
#displaying output
print("Your answere is : ",result)
