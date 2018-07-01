#1.5.12 sum(sum(Lofl, []))
#1.5.13
#[x,y,z]=[4*2,4*1,4*3,4*4]
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: too many values to unpack (expected 3)

#1.5.14
#[(x,y,z) for x in S for y in S for z in S if x+y+z==0]

#1.5.15
#[(0, 2, -2), (0, -2, 2), (1, 1, -2), (1, -2, 1), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -2, 0), (-4, 2, 2), (-2, 0, 2), (-2, 1, 1), (-2, 2, 0)]

#1.5.16
#cannot understand the problem

#1.5.17
#L=[1,1,2,3]
#L
#[1, 1, 2, 3]
#len(L)
#4
#len(list(set(L)))
#3

#1.5.18
#[x for x in list(range(100)) if x%2 == 1]

#1.5.19
#list(zip(list(range(len(L))), L))

#1.5.20
#[x + y for (x, y) in zip([10, 25, 40], [1, 15, 20])]

