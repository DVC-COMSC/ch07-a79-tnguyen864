
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])

# Get sum of rows and print
print ('Sum of rows: ', end=' ')
for i in range(rnum):
	rsum = sum(numbers[i])
	print (rsum, end=' ')
print()

# Get sum of columns and print
print ('Sum of columns: ', end = ' ')
for i in range (cnum):
    csum = 0
    for j in range(rnum):
        csum += numbers[j][i]
    print(csum, end = ' ')
print()

# Find row index number that has greatest sum and print
rowSum = []
print ('The row that has greatest sum: ', end = ' ')
for i in range(rnum):
    rsum = sum(numbers[i])
    rowSum.append(rsum)
print(rowSum.index(max(rowSum)))

# Find greatest number in list and print
maxOfList = max(max(numbers))
print ('The greatest number: ', maxOfList)
