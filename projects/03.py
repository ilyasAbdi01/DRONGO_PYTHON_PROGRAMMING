def multiplication():
    num = int(input('Enter any number between 1 to 10:  '))
    for i in range(1, 11):
        answer = num*i
        print(f'{num} * {i} = {answer}')


multiplication()
