"""

dict={}
que=[1, 1, 2, 3, 4, 2, 1]
ans=[]

for x in que:
    if x not in dict:
        dict[x]=1
    else:
        dict[x]+=1
print(dict)

for x in range(0,len(que)):
    ans.append(-1)
    for y in range(x+1,len(que)):
        
        if dict[que[x]]<dict[que[y]]:
            ans.pop()
            ans.append(que[y])
            break
print(que)
print(ans)

"""
def knows(A,B):
    return (matrix[A][B])
def confirm(C):
    for i in range (0,len(matrix)):
        if matrix[C][i]!=0:
            return 0
    return 1

matrix = [ [ 0, 0, 1, 0 ], 
           [ 0, 0, 1, 0 ], 
           [ 0, 1, 0, 0 ], 
           [ 0, 0, 1, 0 ] ] 
stack=[]
for i in range(0,len(matrix)):
    stack.append(i)
print(stack)

while len(stack)!=1:
    A=stack.pop()
    B=stack.pop()
    if knows(A,B):
        stack.append(B)
    else:
        stack.append(A)
if confirm(stack[0]):
    print("Celebrity Matrix")
else:
    print("Not Celebrity")




        


  





        
        