def factorial():
    num = int(input('Enter any number: '))
    factorial = 1
    if num < 0:
        print("Sorry factorial does not not exist for negative number")
    elif num == 0:
        print('Factorial number is 1') 
    else :
        for i in range (1,num + 1):
            factorial = factorial * i
        print('The factorial of ', num ,'is', factorial)  

factorial()                 