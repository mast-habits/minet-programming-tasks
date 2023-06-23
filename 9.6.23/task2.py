while True:
  
    print("\n\n")
    print("Welcome to the menu based calc involving addition subtraction multiplication division")
    print("enter 69 as first number and 420 as second number to exit any mode\n")
    
    whichOperation = (input("""Enter the number corresponding to the operation you would like to perform: 
1: Addition
2: Subtraction
3: Multiplication
4: Division \n
>>> """))
    
    if whichOperation == "1":
      print("\nwelcome to addition\n")
      run = True
      while run:
        firstNumber=int(input("Enter the first number: "))
        secondNumber=int(input("Enter the second number: "))
        print(f"{firstNumber} + {secondNumber} = {firstNumber+secondNumber}\n")
        
        if firstNumber==69 and secondNumber==420:
          run=False
          
    elif whichOperation == "2":
      print("\nwelcome to subtraction\n")
      run = True
      while run:
        firstNumber=int(input("Enter the first number: "))
        secondNumber=int(input("Enter the second number: "))
        print(f"{firstNumber} - {secondNumber} = {firstNumber-secondNumber}\n")
        
        if firstNumber==69 and secondNumber==420:
          run=False
          
    elif whichOperation == "3":
      print("\nwelcome to multiplication\n")
      run = True
      while run:
        firstNumber=int(input("Enter the first number: "))
        secondNumber=int(input("Enter the second number: "))
        print(f"{firstNumber} x {secondNumber} = {firstNumber*secondNumber}\n")
        
        if firstNumber==69 and secondNumber==420:
          run=False
          
    elif whichOperation == "4":
      print("\nwelcome to division\n")
      run = True
      while run:
        firstNumber=int(input("Enter the first number: "))
        secondNumber=int(input("Enter the second number: "))
        print(f"{firstNumber} ÷ {secondNumber} = {firstNumber/secondNumber}\n")
        
        if firstNumber==69 and secondNumber==420:
          run=False
          
    else:
      print("Check your number again")