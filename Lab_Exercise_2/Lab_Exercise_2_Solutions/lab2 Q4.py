# 4. Given three integers, print the smallest one. (Three integers should be user input)

# user input
int1st = int(input('Enter the 1st integer : '))
int2nd = int(input('Enter the 2nd integer : '))
int3rd = int(input('Enter the 3rd integer : '))


# function
def check():
    # conditions
    if int1st < int3rd and int1st < int2nd:
        print('The smallest integer is ', int1st)
    elif int2nd < int3rd:
        print('The smallest integer is ', int2nd)
    else:
        print('The smallest integer is ', int3rd)


# call function
check()
