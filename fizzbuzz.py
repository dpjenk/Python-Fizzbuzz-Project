def fizzbuzz(n):    # defines the function
    """
    Prints numbers from 1 to n, replacing multiples of 3 with "Fizz", 
    multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".
    """
    for i in range(1, n + 1):
        if i % 15 == 0: # since 3 times 5 is 15, this code is shorter than using "if i % 3 == 0 and i % 5 == 0:""
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(25)    # calls or invokes the function