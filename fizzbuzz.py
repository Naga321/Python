n=int(input("Enter a number"))
if n%3==0 and n%5==0:
    print("Fizzbuzz")
elif n%3==0:
        print("Fizz")
elif n%5==0:
        print("Buzz")
else:
   print("enter proper number")
