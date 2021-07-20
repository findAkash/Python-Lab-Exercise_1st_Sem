#1. Write a program that takes three numbers and prints their sum. Every number is given on a separate line.


#it asks user to enter the 1st,2nd and 3rd numbers
number_1=float(input('Enter the 1st number : '))
number_2=float(input('Enter the 2nd number : '))
number_3=float(input('Enter the 3rd number : '))

#funtion for the addition
def Sum():
    sum=number_1+number_2+number_3
    print('Sum of three numbers :',sum)

Sum()
