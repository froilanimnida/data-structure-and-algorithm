"""
3.4.8   LAB   Days of the week
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you –
this name comes from the fact that objects of that class will be able to store and to manipulate
the days of the week.

The class constructor accepts one argument – a string. The string represents the name
of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the
WeekDayError exception (define it yourself; don't worry, we'll talk about the objective
nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly
convert themselves into strings of the same form as the constructor arguments;

the class should be equipped with one-parameter methods called add_days(n) and
subtract_days(n), with n being an integer number and updating the day of week stored
inside the object in the way reflecting the change of date by the indicated number of days,
forward or backward.
all object's properties should be private;
Complete the template we've provided in the editor and run your code and check
whether your output looks the same as ours.

Expected output
Mon
Tue
Sun
Sorry, I can't serve your request.
"""


class WeekDayError(Exception):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()


class Weeker:
    __week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in Weeker.__week:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        if n == 0:
            self.__day = self.__day
            return
        day_index = self.__week.index(self.__day)
        for i in range(n):
            day_index += 1
            if day_index > len(self.__week) - 1:
                day_index = 0

        self.__day = self.__week[day_index]

    def subtract_days(self, n):
        if n == 0:
            self.__day = self.__day
            return
        day_index = self.__week.index(self.__day)
        for i in range(n):
            day_index -= 1
            if day_index == -1:
                day_index = 6

        self.__day = self.__week[day_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")

# Output:
# Mon
# Tue
# Sun
# Sorry, I can't serve your request.
