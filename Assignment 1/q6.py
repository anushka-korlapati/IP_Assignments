
n=int(input("Enter number:"))

def pattern(n):
    for i in range(1,n+1):
        print('*'*i+" "*2*(n-i)+'*'*i)

pattern(n)



