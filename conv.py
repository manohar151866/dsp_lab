x=input("ENter 1st sequence:")
h=input("ENter 2nd sequence:")
xlen=len(x)
hlen=len(h)
y=[]
temp=[]
temp1=[]
for i in range(0,xlen):

	for j in range(0,hlen):
		temp=x[i]*h[j]
		temp1.append(temp)

inc=1
m=[]
for k in range(0,xlen):
	m.append(temp1[k:hlen-1])
	inc +=1
print(y)
print(temp1)
print(m)