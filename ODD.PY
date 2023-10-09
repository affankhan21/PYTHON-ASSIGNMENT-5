"""
Q2Sum of all odd numbers from 1 to n?
CODE:
 
"""
def sumodd(num2):
    sum2=0
    for i in range(1,num2+1):
        if(i%2!=0):
            sum2=sum2+i
        else:
            continue    
    return sum2






res=0
num=int(input("ENTER THE NUMBER YPTO WHICH YOU WANT ODD ADDITION: "))
res=sumodd(num)
print("THE ADDITION OF ODD NUMBERS UPTO ",num ,"IS",res)