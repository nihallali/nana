N=int(input("N="))
i=res=0
while N!=0:
    res=res+(N%2)*(10**i)
    N=N//2
    i+=1
print(f"the binary number= {res}")      
