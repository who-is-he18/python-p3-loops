
#!/usr/bin/env python3#-

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")
def square_integers(int_list):
    return [num ** 2 for num in int_list]#-
def fizzbuzz():
    # code goes here!#-
#-
    pass#-
    for num in range(1, 101):#+
        if num % 3 == 0 and num % 5 == 0:#+
            print("FizzBuzz")#+
        elif num % 3 == 0:#+
            print("Fizz")#+
        elif num % 5 == 0:#+
            print("Buzz")#+
        else:#+
            print(num)#+

