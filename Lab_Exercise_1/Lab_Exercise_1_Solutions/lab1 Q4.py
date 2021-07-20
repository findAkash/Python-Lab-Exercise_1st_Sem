# 4. Given the integer N - the number of minutes that is passed since midnight - how many
# hours and minutes are displayed on the 24h digital clock?
# The program should print two numbers: the number of hours (between 0 and 23)
# and the number of minutes (between 0 and 59).

N = int(input('Enter the time passes since midnight in minute : '))  # it ask the user for input


# function is used
def time():
    passed_time_in_hour = N // 60
    remaining_min = N % 60
    i = 24  # value is initialized for 24 hr
    while passed_time_in_hour >= 24:  # loop is used to convert the hour which are greater or equal to 24
        passed_time_in_hour = passed_time_in_hour - 24  # it subtracts the hour until it satisfied the condition

    return str(passed_time_in_hour) + ' ' + str(remaining_min)  # integer is converted in string and concatenated


print(time())
