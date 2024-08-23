num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

choice = 0
while True:
    print("^-----------------------^")
    print("|  C A L C U L A T O R  |")
    print("|-----------------------|")
    print("|--- 1. Addition -------|")
    print("|-----------------------|")
    print("|--- 2. Subtraction ----|")
    print("|-----------------------|")
    print("|--- 3. Multiplication -|")
    print("|-----------------------|")
    print("|--- 4. Division -------|")
    print("|-----------------------|")
    print("|--- 5. Exit -----------|")
    print("|-----------------------|")
    choice = int(input("enter your choice: "))
    
    if choice == 1:
        num_add = num1 + num2
        print(f"\nAddition of {num1} and {num2} is: {num_add}\n")
        
    elif choice == 2:
        num_sub = num1 - num2
        print(f"\nSubtraction of {num1} and {num2} is: {num_sub}\n")
        
    elif choice == 3:
        num_mul = num1 * num2
        print(f"\nMultiplication of {num1} and {num2} is: {num_mul}\n")
        
    elif choice == 4:
        num_div = num1 / num2
        print(f"\nDivision of {num1} and {num2} is: {num_div}\n")
        
    elif choice == 5:
        print("\nProgram Exit\n")
        break
    
    else:
        print("\nInvalid choice.Please Try Again\n!!!")
    
    break