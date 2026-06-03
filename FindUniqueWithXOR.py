def findunique(arr,n):
    result=0
    for i in arr:
        result^=i
    return result

def findUniqueusingDict(arr, n) :
    keys={}
    for num in arr:
        keys[num]=keys.get(num,0)+1
    for key,value in keys.items():
        if value==1 :
            return key