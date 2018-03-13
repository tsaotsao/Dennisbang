formatter='%d×%d=%d'
 
for i in range(1,10):
    for j in range(1,10):
            print(formatter%(j,i,i*j),end='\t')
      