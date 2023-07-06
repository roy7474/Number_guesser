import random

#testing samples
# r = random.randrange(-5,11) #random numbers 
# r = random.randint(-5,11) # same as above, but now includes the uppder bound 11 

top_of_range = input('Type a number: ')

if top_of_range.isdigit(): #isdigit is used to confirm that the value entered is a digit
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print('Please type a number larger than 0 next time.')
        quit()

else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)

print(random_number)