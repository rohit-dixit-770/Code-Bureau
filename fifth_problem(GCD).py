def calcGDC(n:int, m: int) -> int:

    # if any of two(n or m) can be smaller
  
    # if n<m:small,large=n,m
    # else:small,large=m,n
    # while small:
    #     large,small=small,large%small
    # return large

   # if "m" is always smaller 
  
    while m:             
        n,m=m,n%m
    return n
