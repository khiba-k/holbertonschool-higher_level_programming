#!/usr/bin/python3
def fizzbuzz():
    num = range(1, 101)
    for x in num:
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz", end=' ')
            continue
        elif x % 3 == 0:
            print("Fizz", end=' ')
        elif x % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(f"{x}", end=' ')
