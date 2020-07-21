# Given a number as an input, print "Fizz" if the number is even, "Buzz" if the number is odd.

num = input("What is your number?: ")
if int(num) % 2 == 0:
    print("Fizz")
else:
    print("Buzz")