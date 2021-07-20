# 5. A school decided to replace the desks in three classrooms.
# Each desk sits two students. Given the number of students in each class,
# print the smallest possible number of desks that can be purchased.
# The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
# In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
# The second group has 21 students, so they can get by with no fewer than 11 desks.
# 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

from math import ceil  # it returns the minimum integer which might be the equal to or greater then the given value

class_a = int(input('Enter the total number of students in class a : '))
class_b = int(input('Enter the total number of students in class b : '))
class_c = int(input('Enter the total number of students in class c : '))


def required_desk():
    desks_for_a = ceil(class_a / 2)
    desks_for_b = ceil(class_b / 2)
    desks_for_c = ceil(class_c / 2)

    return 'The required desk for three classroom are ' + str(desks_for_a + desks_for_b + desks_for_c)


print(required_desk())
