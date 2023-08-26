form ='''name-----><name>
roll---------><roll>
sec----------><sec>
'''

print("enter name roll ans sec")

a=input()
b=input()
c=input()

form=form.replace("<name>",a)
form=form.replace("<roll>",b)
form=form.replace("<sec>",c)

print(form)
