"""
Q4Write a program to print the following fibonnacci series upto n using functions
CODE:"""

def fibo(num5):
    c=0
    print(c,end=" ")
    a=1
    b=0
    for i in range(1,num5):
       
        c=a+b
        print(c,end=" ,")
        a=b
        b=c

num4=int(input("ENTER THE NUMBER N UPTO WHICH YOU WANT FIBONACCI SERIES :"))
fibo(num4)

