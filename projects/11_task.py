def isPalindrome():
    # Name = input('Enter any name: ')
    Name = 'mum'
    return Name[:: -1]


answer = isPalindrome()

if answer:
    print('True')
else:
    print('False')
