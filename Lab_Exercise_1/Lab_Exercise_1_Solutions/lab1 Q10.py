#10. Write a Python program to convert seconds to day, hour, minutes and seconds.

second=int(input('Second : '))
min=0
hour=0
day=0
# class CoversionTime:
#     def __init__(self):
#         self.second=int(input('Enter time in second : '))

while second>=60:
    min+=1
    second=second-60
while min>=60:
    hour+=1
    min=min-60
while hour>=24:
    day+=1
    hour=hour-24


print(day,' day',hour,' hr',min,' min',second, ' sec')