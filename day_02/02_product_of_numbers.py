"""
write a program to display product of number from  1 to n
"""
product=1
n=int(input("enter a number.."))
for i in range(1,n+1):
    product=product*i
print("product=",product)