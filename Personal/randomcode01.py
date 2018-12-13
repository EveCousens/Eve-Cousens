'''
Created on Dec. 13, 2018

@author: s446561
'''
import random

import math
 
randOne = int(input('Enter a value'))
randTwo = int(input('Enter a value'))


rand = random.randint(randOne,randTwo)  

eqN1 = randOne + randTwo / 2

print(rand)

print(eqN1)

randThree = int(input('Enter a value'))
randFour = int(input('Enter a value'))

eqN2 = randThree * randOne + randTwo / randFour * 2 

print(eqN2)

