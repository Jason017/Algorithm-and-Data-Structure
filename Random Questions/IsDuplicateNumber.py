def IsDuplicateNumber(arr):
    s = set()
    for i in range(len(arr)):
        s.add(i)

        if len(s) != i+1:
            return False
    return True

def IsDuplicateNumber1(arr):
    if arr == []:
        return False
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[arr[i]] == arr[i]:
                return True
            temp=arr[arr[i]]
            arr[arr[i]]=arr[i]
            arr[i]=temp
    return False

arr = [4,9,6,3,3]
print(IsDuplicateNumber(arr))