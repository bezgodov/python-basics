reply = int(input())

if reply % 3 == 0 and reply % 5 == 0:
    print("FizzBuzz")
elif reply % 3 == 0:
    print("Fizz")
elif reply % 5 == 0:
    print("Buzz")
else:
    print("")