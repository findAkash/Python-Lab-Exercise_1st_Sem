# 2. WAP which accepts marks of four subjects and display total marks, percentage and grade.

# marks of four subject:
print('Marks')
english = int(input('English : '))
math = int(input('Math : '))
science = int(input('Science : '))
nepali = int(input('Nepali : '))

total_marks = english + math + science + nepali
print('Total Mark = ',total_marks)
percent = total_marks / 4
print('Percentage = ',percent)

def grade():  #function is used for grade
    if percent >= 90:   #conditions for A grade to G grade
        print('Grade = A')
    if 90 > percent >= 80:
        print('Grade = B')
    if 80 > percent >= 70:
        print('Grade = C')
    if 70 > percent >= 60:
        print('Grade = D')
    if 60 > percent >= 50:
        print('Grade = E')
    if 50 > percent >= 40:
        print('Grade = F')
    if 40 > percent >= 0:
        print('Grade = G')

grade() #function is called for the grade