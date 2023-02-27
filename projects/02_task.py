def BMI():
    mass = int(input('Enter your body mass in (lbs):  '))
    height = int(input('Enter your height in (inches):  '))

    BMI = (mass/height)*703

    if BMI < 15:
        print("Severely underweight")
    elif 15 <= BMI < 16:
        print("Underweight")
    elif 16 <= BMI < 18:
        print("Normal")
    elif 18 <= BMI < 25 :
        print('Overweight')
    elif 25 <= BMI < 30:
        print("Obese Class I")
    elif 30 <= BMI < 40:
        print("Obese Class II")
    else:
        print('Very severely overweight') 

BMI()                          