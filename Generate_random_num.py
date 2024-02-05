import random

# generate list of 100000 random numbers between 1 and 300000
random_list = [random.randint(1, 300000) for _ in range(100000)]

# write list to file
with open('random_numbers.txt', 'w') as f:
    for num in random_list:
        f.write(str(num) + '\n')
