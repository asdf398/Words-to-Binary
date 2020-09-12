import numpy as np

t=input("plz enter a sentence")
r=t.split()
#print(r)
z=list(r)
g=list(r)
#print(z)
m=len(r)
i=0
u=0
#loop to find distinct items.
for i in range(0,int(m)):
	for j in range(i+1,int(m)):
		if( z[j]==["False"]):
			continue
		elif(z[j]==z[i]):
			u=u+1
			z[j]=["False"]
#print(u)
distinct = m-u
#print(distinct)
a=np.zeros([int(m),int(distinct)],dtype=int)
#print(a)
y=np.zeros([int(distinct),int(distinct)],dtype=int)
#print(y)
#loop for assigning 1 and 0
i=0
for i in range(0,int(m)):
	 j=0
	 for j in range(0,int(distinct)):
	 	if j==i:
	 		a[i][j]=1
	 		y[i][j]=1
	 	else:
	 		a[i][j]=0
#print(a)
i=0
#loop for checking
for i in range(0,int(m)):
	 j=0
	 for j in range(i,int(m)):
	 	if r[j]==r[i]:
	 	      a[j]=a[i]    
#print(a)
print("the unit matrix is:\n")
#print(y)	
for i in range(0,int(m)):
	for j in range(i+1,int(m)):
		if g[i]==g[j]:
			g[j]=["False"]
print(g)
	
for i in range(0,int(m)):
	if g[i]==["False"]:
		for j in range(i+1,int(m)):
			if g[j]!=["False"]:
				g[i]=g[j]
				g[j]=["False"]
				break
t=list(g[0:int(distinct)])
print(t)
for i in range(0,int(distinct)):
	for j in range(0,int(m)):
		if t[i]==r[j]:
			a[j]=y[i]
print(a)
			

	 		
	 		
	
	
			
			
	
	