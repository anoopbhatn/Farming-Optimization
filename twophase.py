
def minimumfind(temp):
	m=temp[0]
	for i in temp:
		if i>0 and i<m:
			m=i
	return m

print 'Enter first number'
a=input()

print 'Enter second number'
b=input()

a1=[0 for i in range(3)]
b1=[0 for i in range(3)]
c1=[0 for i in range(3)]

print 'First constraint'
print 'Enter a1,b1 and c1'
a1[0],b1[0],c1[0]=raw_input().strip().split(' ')
a1[0],b1[0],c1[0]=[int(a1[0]),int(b1[0]),int(c1[0])]

print 'Second constraint'
print 'Enter a2,b2 and c2'
a1[1],b1[1],c1[1]=raw_input().strip().split(' ')
a1[1],b1[1],c1[1]=[int(a1[1]),int(b1[1]),int(c1[1])]

print 'Third constraint'
print 'Enter a3,b3 and c3'
a1[2],b1[2],c1[2]=raw_input().strip().split(' ')
a1[2],b1[2],c1[2]=[int(a1[2]),int(b1[2]),int(c1[2])]

# First Phase

mat=[[0 for x in range(7)] for y in range(4)]

a2=-(a1[0])-(a1[1])
b2=-(b1[0])-(b1[1])
c2=c1[0]+c1[1]

mat[0][0]=-a2
mat[0][1]=-b2
mat[0][2]=-1
mat[0][6]=c2

for i in range(1,4):
	mat[i][0]=a1[i-1]
for i in range(1,4):
	mat[i][1]=b1[i-1]

mat[2][2]=-1
mat[3][3]=1
mat[1][4]=1
mat[2][5]=1

for i in range(1,4):
	mat[i][6]=c1[i-1]

maxi=mat[0].index(max(mat[0][0:6]))

indv=dict()

while mat[0][maxi]>0 and maxi<6:
	temp= [0 for i in range(3)]
	for i in range(3):
		try:
			temp[i]=(mat[i+1][6]/float(mat[i+1][maxi]))
		except:
			print 'Zero Error'
	mini=minimumfind(temp)
	pivot=(temp.index(mini))+1
	div=mat[pivot][maxi]
	indv[maxi]=pivot
	for i in range(7):
		try:
			mat[pivot][i]=mat[pivot][i]/float(div)
		except:
			print 'Zero Error1'
	for i in range(4):
		if i==pivot:
			continue
		num=mat[i][maxi]
		for j in range(7):
			mat[i][j]-=(num*mat[pivot][j])
			mat[i][j]=round(mat[i][j],10)
	maxi=mat[0].index(max(mat[0][0:6]))

#Second Phase

second=[[0 for x in range(5)] for y in range(4)]

x3=-((a*(-mat[indv[0]][2]))+(b*(-mat[indv[1]][2])))
x4=-((a*(-mat[indv[0]][3]))+(b*(-mat[indv[1]][3])))
c=(a*mat[indv[0]][6])+(b*mat[indv[1]][6])

second[0][2]=x3
second[0][3]=x4
second[0][4]=c

for i in range(1,4):
	for j in range(4):
		second[i][j]=mat[i][j]
for i in range(1,4):
	second[i][4]=mat[i][6]

maxi=second[0].index(max(second[0][0:4]))

indv1=dict()
print maxi
while second[0][maxi]>0 and maxi<4:
	temp= [0 for i in range(3)]
	for i in range(3):
		try:
			temp[i]=(second[i+1][4]/float(second[i+1][maxi]))
		except:
			print 'Zero Error'
	mini=minimumfind(temp)
	pivot=(temp.index(mini))+1
	div=second[pivot][maxi]
	indv1[maxi]=pivot
	for i in range(5):
		try:
			second[pivot][i]=second[pivot][i]/float(div)
		except:
			print 'Zero Error1'
	for i in range(4):
		if i==pivot:
			continue
		num=second[i][maxi]
		for j in range(5):
			second[i][j]-=(num*second[pivot][j])
			second[i][j]=round(second[i][j],10)
	maxi=second[0].index(max(second[0][0:4]))

for i in range(4):
	for j in range(5):
		print second[i][j],
	print 

print 'Optimal solution is '+str(second[0][4])+' with x1 = '+str(second[indv[0]][4])+' and x2 = '+str(second[indv[1]][4])