# 2. Write a program that reads the length of the base and the height of a right-angled triangle and prints
# the area. Every number is given on a separate line.


def formula():                                                              #function is used
    base=float(input('Enter the Base of right-angled triangle : '))         #user input
    height=float(input('Enter the height of right-angled triangle : '))     #user input

    area_of_RAT=(1/2)*base*height                                           #formula fto calculate the area of triangle

    return area_of_RAT

print(formula())                                                            #call the fuction for output


