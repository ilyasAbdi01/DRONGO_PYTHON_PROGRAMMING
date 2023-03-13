def divide_apple():
    num_apples = int(input('Enter the numbers of apples you have: '))
    num_people = int(input('Enter the number of people you are: '))
    result = num_apples//num_people
    print('Each person will gets', result, 'apples')
    mod = num_apples % num_people
    print('The number of apples left are', mod)
      
divide_apple()    