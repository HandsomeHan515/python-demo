class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score

    def getAge(self):
        return self.age

    def getScore(self):
        return self.__score

    def setScore(self, score):
        self.__score = score
        return self.__score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value
        return self.__score


han = Student("hanshuai", 23, 150)
print(han.score)

han.score = 149
print(han.score)

# print(han.getAge())
# print(han.name)

# print(han.getScore())
# # print(han.__score)

# print(han.setScore(146))
# print(han.getScore())


# class Address(Student):
#     def __init__(self, name, age, score, address):
#         super(Address, self).__init__(name, age, score)
#         self.address = address

#     def getAge(self):
#         return self.age

#     def getAdd(self):
#         return self.address


# address = Address('hanshuai', 23, 150, '北京朝阳')
# print(address.getAdd())
# print(address.getAge())
