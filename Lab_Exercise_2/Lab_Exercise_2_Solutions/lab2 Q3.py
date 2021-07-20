#3. Check whether the user input number is even or odd and display it to user.

#user input
user_input=int(input('Enter the number : '))

#conditions
if user_input%2==0:
    print(user_input,'is even')
else:
    print(user_input,'is odd')