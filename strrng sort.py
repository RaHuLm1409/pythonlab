x=input('enter the alphanumeric string ')
l=len(x)

dige= []
digo= []
sml=[]
cap=[]
res=[]

y=[x[i:i+1] for i in range(0, l, 1)]

for i in y:
    if(ord(i)>=97 and ord(i)<=123):
       sml.append(i)
    elif(ord(i)>=65 and ord(i)<=91):
        cap.append(i)
    elif(ord(i)>=48 and ord(i)<=57):
        if(ord(i)%2==0):
            dige.append(i)
        else:
            digo.append(i)
        

dige.sort()
digo.sort()
cap.sort()
sml.sort()

res=sml+cap+digo+dige

for _ in res:
    print(_, end="")



    



