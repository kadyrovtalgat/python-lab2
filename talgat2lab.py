import re
file=open('access.log')
t=[]
p=0
i=-1
for line in file.readlines():
	f=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',line)
	i=1
	for w in f:
		t.insert(i,w)
		i=i+1 
sx=[]
for i in range(0,len(t)):
	f=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.)',t[i])
	p=1
	for w in f:
		sx.insert(p,w)
		p=p+1 						
sx=list(set(sx))
k=0
gr={}
for i in range(0,len(sx)):
	print()
	for p in range(0,len(t)):
		if t[p].find(sx[i])!=-1:
			gr[i,k]=t[p]
			print(gr[i,k])
			k=k+1

	