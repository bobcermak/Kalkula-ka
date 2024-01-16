import time


while True:
    
    try:
        number1 = float(input("Zadejte číslo: "))
        number2 = float(input("Zadejte číslo: "))
        symbol = input("Zadejte symbol: ")
        
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
                result = float(number1) / float(number2)
                print("Váš výsledek je " + str(result))
                
                
          
                 
        math()

        
        choice = str(input("Budete mě ještě znova potřebovat?: (y/n): "))
        if choice == "n":
            print("Mějte se hezky, zatím nashledanou :)")
            time.sleep(1)
            break
        else:
            print("Jdeme na další čísla :)")
        
        
        
        
    except ValueError:
        time.sleep(1)
        print("Zadal jste špatný znak!")