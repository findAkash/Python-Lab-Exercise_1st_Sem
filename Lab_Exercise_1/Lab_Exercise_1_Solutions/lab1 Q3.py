#3. N students take K apples and distribute them among each other evenly.
# The remaining (the undivisible) part remains in the basket. How many apples will each single student get?
# How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for the questions above.

#user input
N=int(input('Enter the number of students : '))
K=int(input('Enter the available apples : '))

#used function
def get_apple():
    distributed = K//N                                                              #formaula is used
    return 'Each student is get '+str(distributed)+' apple.'                        #intiger is converted into string to concatenate

def remain_apple():
    reamin = K % N                                                                      #formaula is used
    return 'Remaining apple in the basket is '+str(reamin)                          #intiger is converted into string to concatenate

print(get_apple())                                                                  #it runs the print the get_apple() funtion
print(remain_apple())                                                               #it runs and print the remain_apple() function