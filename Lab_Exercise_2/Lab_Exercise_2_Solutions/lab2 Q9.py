#10.  Write a Python program to sum of three given integers.
# However, if two values are equal sum will be zero.

a=int(input('1st integer : '))
b=int(input('2st integer : '))
c=int(input('3st integer : '))
sum=a+b+c

if a!=b and a!=c and b!=c: #it checks weather the any two of given integers are equal or not
    print(sum)
else:
    print('sum = 0')

