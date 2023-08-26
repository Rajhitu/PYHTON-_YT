def greatest(a,b,c):
    if(a>b):
      t=a
    else:
      t=b
    if(t>c):
      return t
    else:
      return c



print("enter 3 no.s")
a=int(input())
b=int(input())
c=int(input())

print(f"greatest no. is {greatest(a,b,c)}")
