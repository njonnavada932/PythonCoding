def findTriplet(arr, n, x) :
    total=0
    # for i in range (n-2) :
    #     seen=set()
    #     for j in range (i+1,n) :
    #         expected=x-(arr[i]+arr[j])
    #         if expected in seen :
    #             total+=1
    #         seen.add(arr[j])
    for i in range(n-2) :
        freq={}
        for j in range (i+1,n) :
            expected=x-(arr[i]+arr[j])
            total+=freq.get(expected,0)
            freq[arr[j]]=freq.get(arr[j],0)+1

    return total