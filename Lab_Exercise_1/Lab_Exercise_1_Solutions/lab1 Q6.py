#6. Solve each of the following problems using Python Scripts.
# Make sure you use appropriate variable names and comments.
# When there is a final answer have Python print it to the screen.
# A person’s body mass index (BMI) is defined as: BMI=mass in kg / (height in m)2.
print('Calculate the Person body mass index(BMI)')

mass=float(input('Enter your mass in kg: '))
height=float(input('Enter your height in meter: '))

def find():
    BMI=mass/(height/2)

    return 'Your body mass index (BMI) is '+str(BMI)

print(find())
