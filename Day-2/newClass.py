# IMPORTANT : Regular methods have (self), class methods have (cls), and static methods dont have anything

# STUDENT CLASS

import datetime

rollNumber = 0

class student:
    rollNumber = 0
    fees = 3000
    waiver = 0.8

    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        student.rollNumber += 1
        self.rollNumber = student.rollNumber

    def displayAllInfo(self):
        print(self.name + "\n" + str(self.rollNumber) + "\n" + str(self.phoneNumber) + "\n" + self.email)

    def feeDeduction(self):
        self.fees = int(self.fees * self.waiver)

    # using class methods

    @classmethod
    def changeWaiver(cls, newWaiver):
        cls.waiver = newWaiver

# alternative constructor or class method
    @classmethod
    def fromInput(cls, joinedInput):
        name, phoneNumber, email = joinedInput.split()
        return cls(name, phoneNumber, email)

# use static methods when you dont use class variables or functions

    @staticmethod
    def isOff(day):
        if day.weekday() < 5:
            return False
        else:
            return True

firstStudent = student("Zohaib Ahsan", 3082106908, "zaptekofficial@gmail.com")

secondStudent = student("Ali Haider", 3123123123, "aliofficial@gmail.com")

print(firstStudent.fees)

firstStudent.feeDeduction()

print(firstStudent.fees)

# For getting all info about class/instance

'''

print(firstStudent.__dict__)

print(student.__dict__)

# for changing class variable's value

'''

'''print(firstStudent.waiver)

student.changeWaiver(300)

print(firstStudent.waiver)

print(secondStudent.waiver)
'''

# for alternative method

thirdStudent = student.fromInput("Talha 3153243242 talha@gmail.com")

#print(thirdStudent.__dict__)

print(student.isOff(datetime.date(2019, 5, 19)))