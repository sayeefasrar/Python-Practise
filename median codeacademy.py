def median(x):
    x.sort()
    #print x
    for i in x:
        if len(x)%2 == 0:
            mid=len(x)/2
            #print (x[mid-1] + x[mid])
            mediann=(x[mid-1] + x[mid])/2.0
        else:
            mid= int(round( len(x)/2))
            mediann= x[mid]
    return mediann
#x=[4,5,5,4]
#print median(x)
