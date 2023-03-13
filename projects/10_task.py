def seconds_to_hour_miunte():
    num_seconds = int(input('Enter the number of seconds passed in the day so far:  '))
    num_hours = num_seconds // 3600
    num_minutes = (num_seconds % 3600) // 60 
    seconds = (num_seconds % 3600) % 60
    


    print('current hour is ', num_hours)
    print('current minute is', num_minutes)
    print('current seconds is', seconds)


seconds_to_hour_miunte()
