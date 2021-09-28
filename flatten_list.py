def helper(lst,slate):
    if type(lst) == type(list()):
        for i in lst:
            if type(i) == type(list()):
                helper(i,slate)
            else:
                
                slate.append(i)
    else:
        
        slate.append(lst)
    

lst = [1,2,3,[4,[5,6],[7,8,[9]]],10]
slate = []

helper(lst,slate)
print(slate)