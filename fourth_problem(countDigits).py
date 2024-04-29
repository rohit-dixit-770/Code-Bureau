def countDigits(n: int) -> int:
    num,count=n,0
    while num!=0:
        digit=num%10
        if digit!=0 and n%digit==0:count+=1
        num=num//10
    return count
