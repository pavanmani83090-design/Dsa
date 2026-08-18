def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quick(arr,low=0,high=None):
    if high is None:
        high=len(arr)-1
    if low<high:
        q=partition(arr,low,high)
        quick(arr,low,q-1)
        quick(arr,high,q+1)
m=[]
n=int(input("Enter number: "))
for _ in range(n):
    val=int(input())
    m.append(val)
result=quick(m)
print("Quick sort: ",m)
