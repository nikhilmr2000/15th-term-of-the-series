

#Find the 15th term of the series?

#0,0,7,6,14,12,21,18, 28

n=0
p=0
m=0
l=[]
while(n>=0):
    if(n%2==0):
        if(n>0):
            p+=7
            l.append(p)
        else:
            l.append(0)
    else:
        if(n>1):
            m+=6
            l.append(m)
        else:
            l.append(0)
    n=n+1
    if(n==15):
        break
print(l[-1])
            
        


