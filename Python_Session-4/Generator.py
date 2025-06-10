# A generator is a function that returns an iterator, producing a sequence of values one at a time, when iterated over
# Generators are memory efficient as they do not store all values in a memory.

def my_generator_func(x):
    value = 0
    while value < x:
        yield value
        value += 1

for i in my_generator_func(3):
    print(i)

