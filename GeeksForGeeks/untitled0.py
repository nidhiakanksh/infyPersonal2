arr = [60864,25176,27249,21296,20204]
target = 56803


sol_arr_abs=[]
sol_arr=[]
if sum(arr)==target:
    print(max(arr))
    

def manipulate_arr(x):
    arr1=arr[:]
    for i in range (0,len(arr1)):
        if arr1[i]>x:
            arr1[i]=x
    print(arr1)
    return sum(arr1)

for x in arr:
    sol_arr.append(manipulate_arr(x))

print(sol_arr)
for i in range(0,len(sol_arr)):
    sol_arr[i]-=target
    sol_arr_abs.append(abs(sol_arr[i]))

print(sol_arr)
print('abs',sol_arr_abs)
minimum=min(sol_arr_abs)

if sol_arr_abs.count(minimum)>1:
    ind=sol_arr.index(-1*minimum)
else:
    ind=sol_arr_abs.index(minimum)
    
print(arr[ind])