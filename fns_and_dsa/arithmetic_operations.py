def perform_operation(num1, num2, operation):

  numb1 = float(input("Enter the first number: "))
  numb2 = float(input("Enter the second number: "))


  operation = input("enter the operation (add, subtract, multiply, divide): ").lower()
   
  match operation:
   
   case "add":
     print(f"Result: {numb1 + numb2} ")
   
   case "subtract":
     print(f"Result: {numb1 - numb2}" )

   case "multiply":
     print(f"Result: {numb1 * numb2}" )

   case "divide":
            if numb2 == 0:
                return "Error: Division by zero!"
            else:
                return numb1 / numb2

perform_operation()
  
   
 
