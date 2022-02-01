import math
def PerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x


n=int(input("Enter to check the number if it is fibonacci or not"))
result1=5*(n*n)+4
result2=5*(n*n)-4

if PerfectSquare(result1)or PerfectSquare(result2):
    print(n, "is fibonacci number")
else:
    print(n, "is not fibonacci number")
