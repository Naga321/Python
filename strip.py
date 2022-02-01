a=set()
b=set()
c={7,8,9,1,2,3,4,5,0}
a.update(c)
print(a)
d={4,5,6,0}
b.update(d)
print(b)
print(b.issubset(a))
print(a.isdisjoint(b))
a.discard(8)
print(a)

