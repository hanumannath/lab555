import math
a=int(input())
b=int(input())
c=int(input())
sqrt=math.sqrt
pow=math.pow
disc=sqrt((pow(b,2))-4*a*c)
if(disc>0):
    x=(-b+disc)/(2*a)
    y=(-b-disc)/(2*a)
    print("Roots are",x,y)
elif (disc==0):
    print("Roots are",(-b)/(2*a))
else:
    print("Roots doesn't exsit")                                                                                                                                                                                                                            