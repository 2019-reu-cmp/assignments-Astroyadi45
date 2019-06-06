'''Performs dot product'''
a=[1,2,3]
b=[2,5,10]

dot=0
for i,x in enumerate(a):
    dot+=b[i]*x
print(dot)

dot=0
for c in zip(a,b):
    calc=c[0]*c[1]
    dot+=calc
print(dot)

