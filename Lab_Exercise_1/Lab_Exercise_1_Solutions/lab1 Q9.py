#Write a python program to find sum of the first
# n positive integers.
#sum = (n*(n+1))/2
class FirstNo:
    def __init__(self):
        self.n = int(input('Enter the positive number : '))

    def find(self):
        sum = (self.n*(self.n+1))/2
        print('Sum of the first',self.n,'positive number : ',sum)

a=FirstNo()
a.find()