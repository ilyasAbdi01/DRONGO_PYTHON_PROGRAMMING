def BOGO():
    First_input = int(input('Enter the cost of the expensive item: '))
    second_input = int(input('Enter the cost of the cheap item:   '))

    if First_input > second_input:
        descount = second_input * 0.5
        total = descount + First_input
        print(total)

    else:
        total = First_input + second_input
        print(total)


BOGO()
