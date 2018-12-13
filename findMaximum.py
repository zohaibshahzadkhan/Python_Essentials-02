print("Enter the first number");
firstNumber = int(input());
print("Enter the second number");
secondNumber = int(input());

if firstNumber > secondNumber:
  print("{} is greater than {}".format(firstNumber,secondNumber));
else: 
  print("{} is greater than {} ".format(secondNumber,firstNumber));