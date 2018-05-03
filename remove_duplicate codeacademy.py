def remove_duplicates(x):
    no_dupl=[]
    for i  in x:
        if i not in no_dupl:
            no_dupl.insert(0, i)
        
    return (no_dupl)
n=[1,1,1,1,1, 2,3,5,2,3,6,5,7]
print (remove_duplicates(n))
