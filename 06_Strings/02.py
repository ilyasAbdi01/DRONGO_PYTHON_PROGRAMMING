def more_on_strings():
    message = "Welcome to Drongo"
    len_str = len(message)
    print(len_str)


    # using index to access characters
    print(message[4]) # positive indexing within the range
    print(message[-2]) # negative indexing within the range
    

    #slicing a string 
    print(message[2:5]) # positve  slicing
    print(message[-10:-2]) # negative slicing
    print(message[:5]) # slicing from the start
    print(message[2:]) # slicing to the end 

more_on_strings()    