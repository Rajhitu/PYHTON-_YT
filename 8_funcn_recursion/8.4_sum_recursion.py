def sum_rec(n):

    if(n==1):
      return 1
    else:
        return n+sum_rec(n-1)

n=int(input("enter ur no."))

print(f"sum of 1st {n} natural no. is {sum_rec(n)}")