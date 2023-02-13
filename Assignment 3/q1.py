n=int(input("Enter no:"))

def pattern_up(n, x=0):
    
    
    if n>=1:
        print("* "*n+" "*(x)+"* "*n)
        return pattern_up(n-1,x+4)

    else:
        return x-8

x=pattern_up(n)

a=2

def pattern_down(a,x):

    print("* "*a+" "*(x)+"* "*a)

    if a<n:
        return pattern_down(a+1,x-4)

    else:
        pass

pattern_down(a,x)
