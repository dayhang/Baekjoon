def merge_sort(a):
    if len(a) == 1:
        return a
    
    mid = (len(a)+1)//2
   
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    i,j = 0,0
    a_sorted = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_sorted.append(left[i])
            b_sorted.append(left[i])
            i+=1
        else:
            a_sorted.append(right[j])
            b_sorted.append(right[j])
            j+=1
    while i < len(left):
        a_sorted.append(left[i])
        b_sorted.append(left[i])
        i+=1
    while j < len(right):
        a_sorted.append(right[j])
        b_sorted.append(right[j])
        j+=1
    
    return a_sorted

b_sorted = []
n, k = map(int,input().split())
arr = list(map(int,input().split()))
merge_sort(arr)

if len(b_sorted) >= k:
    print(b_sorted[k-1])
else:
    print(-1)
