exp=input("enter an arithmetic operation:")
a=[]
for i in exp :
    if i=="/"or i=="*"or i=="-"or i=="+":
        a.append(exp[0:exp.index(i)])
        a.append(i)
        exp=exp[exp.index(i)+1:]
a.append(exp)    
print(a)
while len(a)>1:
    for i in a[:]:                                                       
        if i=="/" or i=="*":
            if i=="/":
                a.insert(a.index(i)-1,float(float(a[a.index(i)-1])/float(a[a.index(i)+1])))
                s=a.index(i)
                a.pop(a.index(i))
                a.pop(s)
                a.pop(s-1)
                print(a)
            elif i=="*":
                a.insert(a.index(i)-1,float(float(a[a.index(i)-1])*float(a[a.index(i)+1])))
                s=a.index(i)
                a.pop(a.index(i))
                a.pop(s)
                a.pop(s-1)
                print(a)
    for i in a[:]:
        if i=="+" or i=="-":
            if i=="+":
                a.insert(a.index(i)-1,float(float(a[a.index(i)-1])+float(a[a.index(i)+1])))
                s=a.index(i)
                a.pop(a.index(i))
                a.pop(s)
                a.pop(s-1)
                print(a)
            elif i=="-":
                a.insert(a.index(i)-1,float(float(a[a.index(i)-1])-float(a[a.index(i)+1])))
                s=a.index(i)
                a.pop(a.index(i))
                a.pop(s)
                a.pop(s-1)
                print(a)
print(a)