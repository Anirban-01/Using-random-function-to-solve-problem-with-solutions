"""As an exercise, generate a random number between low and high"""

# Suppose we want to generate random number between [2,4).

import random


def my_random_function():
    return 1 * random.random() + 2


for i in range(10):
    print(random.random())

my_random_function()
