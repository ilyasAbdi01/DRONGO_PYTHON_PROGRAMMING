# recursion is process in which function call itself
# recursive functions are used mostly for sequence generation and are used to make the code the code look clean and elegant.

def rec_sum(n):
    if n <= 1:
        return n
    else :
        return n + rec_sum(n-1)
    

y = rec_sum (4)
print(y)    