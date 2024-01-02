

def operation() :
    x = int(input("enter the value of x:"))
    y = int(input("enter the value of y:"))
    option = {
        'a': x+y,
        'b': x-y,
        'c': x*y,
        'd': x%y
    }
    
    n = input("Enter the option, eg : a = +, b = -, c = *, d = /")

    if(n in option) : 
        print(option[n])
        confirm = input("would you like to use calculator again..?, if yes press y or press any key to quit!")
        if(confirm == 'y') : 
            operation()
        elif (confirm != 'y') : 
            return 0

    else : 
        print("invalid option")
    
        while(True) : 
            n = input("Enter the option, eg : a = +, b = -, c = *, d = /")
            if(n in option) :
                    print(option[n])
                    confirm = input("would you like to use calculator again..?, if yes press y or any key to quit!")
                    if(confirm == 'y') : 
                         operation()
                    elif (confirm != 'y') : 
                         return 0

operation()
            
                
            
                

      
             
        



    
    
