s=input("Enter some string")
i=0
print("The characters at even position is")
while (i<len(s)):
    print(s[i],end=',')
    i=i+2
print()
print("The characters at odd position is")
i=1
while i<len(s):
    print(s[i],end=',')
    i=i+2
    
