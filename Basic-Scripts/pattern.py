rows = int(input("Enter the number of rows "))    

for i in range(1,rows+1):                         
    
    for j in range(1,rows+1):                     
        if(j <= rows-i):                          
            print(' ',end='')
        else:
            if(i%2 != 0):
                print(i,end='')
            else:
                print('#',end='')
    print()
