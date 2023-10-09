"""Q3 Sum of all prime numbers from 1 to n?
CODE:"""

def sumprime(num):
    sum3=0
    for i in range(2,num+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            sum3=sum3+i 
    return sum3    



res=0
num=int(input("ENTER THE NUMBER UPTO WHICH YOU WANT PRIME ADDITION: "))
res=sumprime(num)
print("THE ADDITION OF PRIME NUMBERS UPTO ",num ,"IS",res)
