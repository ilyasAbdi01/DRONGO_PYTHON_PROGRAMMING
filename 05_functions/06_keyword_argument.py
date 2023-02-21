def hello(fname, lname):
    print ("Hello", fname, lname)

hello ('Yaska', 'Ilyas')

def hello(fname, lname):
    print("Hello", fname, lname)

hello(lname='Yaska', fname='Ilyas')

def hello(**name):
    print("Hello", name['fname'], name ['lname'])

hello(fname='Drongo', lname='College')
hello(lname='Google', fname='Pixel')
hello(fname='Kenya', lname='Nairobi')
# hello(fname='Bill') #give error
