def string_operators():
    message1 = "Hello, World!"
    message2 = "Welcome to Drongo"
    print(message1 + message2)
    print(message1 * 3)
    print(message1[6])
    print(message2[:7])
    str1 = 'hello'
    if str1 in message1 : # in operator
        print("It is present!")
    if str1 not in message2: # not in operator
        print("It is not present!")    

string_operators()        