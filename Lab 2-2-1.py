A = [10,9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
count = 0
for i in A:
    if i<0:
        count +=1
print(A)
print("Отрицательные оценки в спискe: ", count)
