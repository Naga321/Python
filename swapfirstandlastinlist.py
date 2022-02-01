list=eval(input("Enter some list"))
print(list)
n=len(list)
temp=list[0]
list[0]=list[n-1]
list[n-1]=temp
print(list)
