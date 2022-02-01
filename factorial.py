def cal_factorial(num):
    factorial = 1
    if num == 0 or num == 1:
        return 1
    for i in range(1,num+1):
        factorial = factorial*i
    return factorial    


num=int(input("Enter number to find factorial"))
output=cal_factorial(num)
print("The factorial of given", num , "is" , output)
