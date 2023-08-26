

for i in range(20):

    with open('table.txt'+str(i),'w') as f:
        for j in range(10):
            x=(i+1)*(j+1);
            
            f.write(str(i+1)+"*"+str(j+1)+"="+str(x))
            f.write("\n")