# half values of tuple in 1 line and other half in next line
tp=(1,2,3,4,5,6,7,8,9,10)
tp3=()
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)
#another tuple whose values are even numbers
for x in tp:
    if x%2==0:
        tp3=tp3+(x,)
print(tp3)
#concatenate t2 with t1
t1=(1,2,3)
t2=(11,13,15)
t2=t2+t1
print(t2)
#max and min value
print("Max element is",max(t2))
print("Min element is",min(t2))
