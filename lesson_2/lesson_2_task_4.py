for fizz_buzz in range(1, 31):
    if (fizz_buzz % 3 == 0) and (fizz_buzz % 5 == 0):
        print("FizzBuzz")
    elif (fizz_buzz % 5 == 0):
        print("Buzz")
    elif (fizz_buzz % 3 == 0):
        print("Fizz")
    else:
        print(fizz_buzz)
