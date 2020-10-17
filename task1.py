# task 1: boolean function for prime number checker
# create random number generator by using random function
# remember to name function "is_prime" 
# no user input


def is_prime (rand_num):
    k = 0
    for i in range (1, 101):
        if rand_num % i == 0:
            k = k + 1 
            if k > 2:
                return False
    return True 

import random 
for i in range (1,7):
    rand_num = (random.randint(1,100))
    if is_prime(rand_num) == True:
        print ("The random number" ,rand_num, "is a prime number.")
    else:
        print ("The random number" ,rand_num, "is not a prime number.")





