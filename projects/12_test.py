values = [10,20,50,10,60,20,10,50,60,10,20,10]
def most_least_frequent(values):
    freq = {}
    for V in values:
        if V in freq:
            freq [V] += 1
        else:
            freq [V] = 1 

    max_freq = None
    min_freq = None
    for V in freq:
        if max_freq is None or freq[V] > max_freq:
            max_freq = freq[V]
            print('There are',freq)
        if min_freq is None or freq [V] < min_freq:
            min_freq = freq[V]
    return max_freq, min_freq

print(most_least_frequent(values))       
    
    
                   
    






  