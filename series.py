"""

Q1Write a program to find sum of following series using functions:
1!+2!+3!+4!..........|+n!?
CODE:
"""






def fact(n):
    f=1
    while (n!=0):
        f=f*n
        n=n-1
    return f     



def sumofseries(n):
    sum1=0
   
    for i in range(1,n+1):
        sum1=sum1+fact(i)
    return sum1    






n=int(input("ENTER THE NUMBER UPTO WHICH YOU WANT ADDITION :"))
rs=0
rs=sumofseries(n)
print("SUM OF SERIES UPTO :",n,"IS",rs)