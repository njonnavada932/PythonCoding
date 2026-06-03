def findUnique(arr, n) :
    keys={}
    for num in arr:
        keys[num]=keys.get(num,0)+1
    for key,value in keys.items():
        if value==1 :
            return key