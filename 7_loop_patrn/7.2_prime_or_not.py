n=int(input("enter a no. to find ehther prime or no: "))
c=0
for i  in range(2,n):
    if(n%i==0):
        c=c+1
        break


if(c>0):
    print("not a prime")
else:
    print(f"yes {n} is a prime no.")
      

