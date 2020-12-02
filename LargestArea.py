'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
nm=input("Enter N & M: ")
nm=list(map(int, nm.split()))
print("Enter Land in Matrix Form: ")
l=[]
a=[]
for i in range(nm[0]):
    r=input()
    l.append(list(map(int, r.split())))
for i in range(nm[0]):
    for j in range(nm[1]):
        if l[i][j]==1:
            c=0
            if i==0:
                c+=1
                if l[i+1][j]==0:
                    c+=1
            elif i==nm[0]-1:
                c+=1
                if l[i-1][j]==0:
                    c+=1
            else:
                if l[i-1][j]==0:
                    c+=1
                if l[i+1][j]==0:
                    c+=1
            if j==0:
                c+=1
                if l[i][j+1]==0:
                    c+=1
            elif j==nm[1]-1:
                c+=1
                if l[i][j-1]==0:
                    c+=1
            else:
                if l[i][j-1]==0:
                    c+=1
                if l[i][j+1]==0:
                    c+=1
            if c!=4:
                a.append(c)
print(len(a))