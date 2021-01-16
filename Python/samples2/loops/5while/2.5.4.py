# -*- encoding: utf-8 -*-
"""
Угадай моё число
"""

import random  

# set the initial values from 1 to 5
the_number = random.randrange(5) + 1
guess = int(raw_input("Take a guess: "))
tries = 1

# guessing loop
while (guess != the_number):
    if (guess > the_number):
        print "Lower..." 
    else:
        print "Higher..." 

    guess = int(raw_input("Take a guess: "))
    tries += 1

print "You guessed it!  The number was", the_number
print "And it only took you", tries, "tries!\n" 
