numb1 = int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))


operation = input("Choose the operation (+, -, *, /): ")


match operation:
 
 case "+":
   print(f"The result is {numb1 + numb2}. ")
 
 case "-":
   print(f"The result is {numb1 + numb2} . ")

 case "*":
   print(f"The result is {numb1 * numb2} . ")

 case "/":
  if numb2 == 0:
   print(f"Cannot divide by zero. ")
  
  else:
   print(f"The result is {numb1 / numb2} . ")

 
 case _:
  print("invalid opertaion")