time = int (input("Enter the time you arrived: "))

if time < 9 :
    print("You are on time")

elif time > 9 and time <= 10:
    print("You are 10 minutes late")

elif time > 10 and time <= 12:
    print("You are 30 minutes late")

else :
    print("Zero marks")        
        