# INHERITANCE

'''
FOR INSTALLING EXTERNAL MODULES

python -m pip install PyQt5


'''

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

# new sub-class
class specialStudent(student):
    waiver = 0.6

# adding another parameter to the constructor
    def __init__(self, name, phoneNumber, email, disabilityType, listOffriends = None):
        super(specialStudent, self).__init__(name, phoneNumber, email)
        self.disabilityType = disabilityType
        if listOffriends is None:
            self.listOffriends = []
        else:
            self.listOffriends = listOffriends

    def addFriend(self, student):
        if student not in self.listOffriends:
            self.listOffriends.append(student)

    def removeFriend(self, student):
        if student in self.listOffriends:
            self.listOffriends.remove(student)

    def printFriends(self):
        for friend in self.listOffriends:
            print(friend.name)

        if self.listOffriends == []:
            print("You have no friends")

# list of friends


firstStudent = student("Zohaib Ahsan", 3082106908, "zaptekofficial@gmail.com")

secondStudent = student("Ali Haider", 3123123123, "aliofficial@gmail.com")

thirdStudent = specialStudent("John Cena", 619619, "arfeen@zohaib.com", "mute")

# secondStudent.feeDeduction()
# thirdStudent.feeDeduction()

# print(secondStudent.fees)
# print(thirdStudent.fees)

#for seeing the method resolution order and other info

#print(help(specialStudent))

# adding new parameter to the child class

# print(thirdStudent.disabilityType)

# New class method in sub class

#print(thirdStudent.listOffriends)

#thirdStudent.addFriend(firstStudent)

#thirdStudent.printFriends()

#thirdStudent.addFriend(secondStudent)

#thirdStudent.printFriends()

#thirdStudent.removeFriend(firstStudent)

#thirdStudent.removeFriend(secondStudent)

thirdStudent.printFriends()

# For checking whether an object is an instance of a class and a subclass belongs to a class

print(issubclass(specialStudent, student))

print(isinstance(firstStudent, student))

print(isinstance(specialStudent, student))

