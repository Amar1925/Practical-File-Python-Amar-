a=[[2,5,7], 
    [3,4,5]]
print(a)
print(a[1][0])
result = [[0,0],
         [0,0],
         [0,0]]
for i in range(len(a)):
   for j in range(len(a[0])):
       result[j][i] = a[i][j]

for r in result:
   print(r)