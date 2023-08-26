temp=1
def fact(n):
    
   if(n==0 or n==1):
     return 1
     
   else:
     temp=fact(n-1)*n*temp


n=int(input("enter the no."))

# print(fact(n))

print(f"factorial of {n} is ={temp}")