def pairSum2(arr, k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    return(' ').join( map(str, list(output)) )
 

pairSum2([1,2,3,4,6,7], 5)