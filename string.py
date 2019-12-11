
import itertools
from random import *
def kbits(n, k):
    
    for bits in itertools.combinations(range(n), k):
        s = ['0'] * n
        for bit in bits:
            s[bit] = '1'
        
    return s

stringvar = kbits(5 ,2) 
print(stringvar) 

'''
def kbits(n, k):
    
    for bits in itertools.combinations(range(n), k):
        bits = bits + randint(1,n)
        s = ['0'] * n 
        for bit in bits
            s[bit] = '1'
        
    return s

#stringvar = kbits(80 , 4) 
#print(stringvar) 
    '''
