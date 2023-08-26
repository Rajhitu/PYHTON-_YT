class calc:
    name="hitu "
    def square(self,n):
        return n*n
    
    def cube(self,n):
        return n*n*n

    def squareroot(self,n):
        return n**(1/2)

    @staticmethod
    def greet():
        print("lora bc")
    # @classmethod
    def change(self,name):
        self.name=name

         


print("press 1 to find sqaure")
print("press 2 to find cube")
print("press 3 to find sqaureroot")
choice=int(input())
n=int(input("enter the number"))
obj=calc()
if choice==1:
    print(f"sqaure of the no. is ={obj.square(n)}")
elif choice==2:
    print(f"sqaure of the no. is ={obj.cube(n)}")
elif choice==3:
    print(f"sqaure of the no. is ={obj.squareroot(n)}")

obj.greet()
calc.greet()
obj.change("procoder")

print(obj.name)
print(calc.name)