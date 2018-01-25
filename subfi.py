p=int(input("enter marks of sub1"))
d=int(input("enter marks of sub2:"))
s=int(input("enter marks of sub3"))
t=int(input("enter marks of sub4:"))
a=int(input("enter marks of sub5:"))
to=((p+d+s+t+a)/500)*100
print(to)
if (to<=100) & (to>80):
    print("o")
elif (to<=80) &(to>70):
    print("A+")
elif (to<=70) &(to>60):
    print("A")
elif (to<=60)&(to>50):
    print("B")
elif (to<=50) &(to>40):
    print("c")
elif to<=40:
    print("D")
    
    
