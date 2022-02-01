s1=input("Enter some string")
s2=input("Enter some string")
i,j=0,0
output=''
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
print(output)        
