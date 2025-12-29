def insertSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=j-1
    while j>0 and arr[j]>key:
        arr[j+1]=arr[j]
        j-=1
        arr[j+1]=key
    return arr
array[3,5,1,8,7,2,100,4,9]
print(insertSort(arr))