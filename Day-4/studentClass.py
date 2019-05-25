# SPECIAL MAGIC/DUNDER METHODS
# DUNDER METHOD IS ONE WHICH IS SURROUNDED BY TWO UNDERSCORES __

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

    def __repr__(self):
        # SIMILAR TO AN INSTANCE
        return "student('{}', '{}', '{}')".format(self.name, self.rollNumber, self.phoneNumber)

    def __str__(self):
        # FOR THE END-USER
        return "{} - {}".format(self.name, self.rollNumber)

    # FOR BUILT-IN DUNDER METHODS

    def __add__(self, other):
        return self.fees + other.fees

    def __len__(self):
        return len(self.name)


firstStudent = student("Zohaib Ahsan", 3082106908, "zaptekofficial@gmail.com")

secondStudent = student("Ali Haider", 3123123123, "aliofficial@gmail.com")

# repr function for altering print and unambiguous representation of a class / is to be seen by other developers
#repr(firstStudent)

# str function for more readable representation / aimed at the end-user
#str(secondStudent)

print(secondStudent)

print(firstStudent.__repr__())

print(firstStudent + secondStudent)

print(secondStudent.__len__())

print(len(firstStudent))


# NEXT TO LEARN POLYMORPHISM, OVERRIDING AND OTHER CONCEPTS