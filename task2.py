# task 2: tuple of two positive ONE-digit intergers
# positive ONE-digit integers = 1,2,3,4,5,6,7,8,9
# needs user input

import random

def rand_tuple ():
    pos_int1 = random.randrange(1,10)
    pos_int2 = random.randrange (1,10)
    return (pos_int1, pos_int2)
pos_int = rand_tuple()
int_product = pos_int[0] * pos_int[1]

while True:
    print("How much is" ,pos_int[0], "times" ,pos_int[1], "?: ")
    answer = int(input())
    if answer == int_product:
        print("Correct, done!")
        break
    else:
        print(pos_int[0], "times" ,pos_int[1], "is not" ,answer, ", please try again!: ")
        continue


