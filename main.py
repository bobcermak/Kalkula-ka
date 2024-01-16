import time


while True:
    
    try:
        number1 = float(input("Zadejte číslo: "))
        number2 = float(input("Zadejte číslo: "))
        symbol = input("Zadejte symbol: +, -, *, /: ")
        
        def math():
            if symbol == "+":
                result = float(number1) + float(number2)
                print("Váš výsledek je " + str(result))
            
            elif symbol == "-":
                result = float(number1) - float(number2)
                print("Váš výsledek je " +  str(result))
                
            elif symbol == "*":
                result = float(number1) * float(number2)
                print("Váš výsledek je " +  str(result))
                 
            elif symbol == "/":
                if number2 == 0:
                    print("Nelze dělit nulou!!!")
                else:
                    result = float(number1) / float(number2)
                    print("Váš výsledek je " + str(result))
                
                
                        
        math()

        
        choice = str(input("Budete mě ještě znova potřebovat?: (y/n): ")).lower()  #VŽDY PSÁT () ZA LOWER ČI UPPER
        if choice == "y":
            print("Jdeme na další čísla :)")
            
        else:
            print("Mějte se hezky, zatím nashledanou :)")
            time.sleep(1)
            break
        
        
        
    except ValueError:
        time.sleep(1)
        print("Zadal jste špatný znak!")