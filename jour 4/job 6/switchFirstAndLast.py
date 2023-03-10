L = [7, 13, 21, 34, 55]

def switch_first_last(lst):
    First = lst[0]
    lst[0] = lst[-1]
    lst[-1] = First
    
    return lst
print(switch_first_last(L))
    


