def diff(n1,n2,n3):
    if n1 < n2 < n3:
        return n3-n1
    elif n2 < n1 < n3:
        return n3 -n2
    elif n3 < n1 < n2:
        return n2 - n3
    elif n1< n3< n2:
        return n2 - n1
    elif n2 < n3 < n1:
        return n1 - n2
    elif n3 < n2 < n1:
        return n3-n1
    
print(diff(2,12,8))