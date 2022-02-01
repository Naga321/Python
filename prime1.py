num=int(input("Enter the number to check"))
if num>1:
    for i in range(2,num):
        if(num%i) == 0:
            print(num," is not prime number")
            break
    else:
        print(num," is prime number")
        
