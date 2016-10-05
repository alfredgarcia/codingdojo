
def OddEven(a,b):
    for num in range(a, b):
        if num % 2 == 0:
            print 'Number is', (str(num)) + '.','This is an even number.'
        else:
            print 'Number is', (str(num)) + '.','This is an odd number.'

OddEven(1,2001)
