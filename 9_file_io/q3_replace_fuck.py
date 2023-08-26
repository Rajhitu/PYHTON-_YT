with open("donkey.txt",'r') as f:
    text=f.read()
print(text)
print("\n")

text=text.replace("donkeu","fuck")

print(text)
with open("donkey.txt",'w') as f:
    text=f.write(text)

