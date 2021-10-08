import random

import colorama

colors = list(vars(colorama.Fore).values())

jackieboy = 'all work and no play makes jack a dull boy. all work and no play makes jack a dull boy. all work and no play makes jack a dull boy.'

#x = 0

#while x < 1000:
while True:
    jackieboy = ''.join(random.choice((x, y)) for x, y in zip(jackieboy.upper(), jackieboy.lower()))
    colored_chars = [random.choice(colors) + char for char in jackieboy]
    print(''.join(colored_chars))
#    x = x + 1
