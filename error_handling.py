def sum(num1, num2):
    while True:
        try:
            return num1+num2
        except  TypeError as err:
            print("You have made a mistake!", err)
        else:
            print("I run if no error or no break")
            print("I also can not come right after try")
        finally:
            print("I run no matter what")
            break
        
sum(1,2)