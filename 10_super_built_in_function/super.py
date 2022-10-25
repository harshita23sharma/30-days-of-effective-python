"""
Initialize the parent class from a subclass using super() instead of __init__

"""

class MyBaseClass:
    def __init__(self, value):
        self.value = value

class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        # super().__init__(value)
        self.value += 9

class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)
        # super().__init__(value)

foo = ThisWay(5)
print("Should be (5*7) + 9 = 44 but is ", foo.value)
#Should be (5*7) + 9 = 44 but is  14
#This is because PlusNine causes value to reset to 5, so ans is 5+9= 14
# To avoid this Python has super built in function & standard method resolution order (MRO)
# super ensures that common subclasses in diamond hierarchies are run only once

class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class ThisWayCorrect(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)

foo_correct = ThisWayCorrect(5)
print("Should be (5*7) + 9 = 44 but is ", foo_correct.value)
# Should be (5*7) + 9 = 44 but is  98, Which is Correct!
# ThisWayCorrect calls TimesSevenCorrect which then calls PlusNineCorrect
# which then calls MyBaseClass. So, the order is 7*(5+9) = 98

# First arg to super is type of class whose MRO parent view you're trying to access
# and then the instance on wich you're trying to access that view
class ThisWayCorrect1(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super(ThisWayCorrect1, self).__init__(value)

# Python compiler automatically provides __class__, self
class ThisWayCorrect2(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super(__class__, self).__init__(value)