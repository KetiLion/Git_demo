# class Dog:
#     biology_class = "Animal"
#     def __init__(self, name, weight, color):
#         self._name = name
#         self.weight = weight
#         self.color = color
#
#     def run(self):
#         return "I can run"
#
#     def get_name(self):
#         return f'Hello, My name is {self._name}'
#     def set_name(self, new_name):
#         self._name = new_name
#
# dog1 = Dog("Bobik" , 5 , "brown")
# # print(dog1.name)
# # print(dog1.get_name())
# # print(dog1.biology_class)
# #
# dog2 = Dog('Rex', 8, "black")
# print(dog2.get_name())
# print(dog2.__dict__)
# # dog2.name = "Mikki"
# print(dog2.get_name())
# # print(dog2.biology_class)
#
# class Pitbull(Dog):
#     def __init__(self, name, weight, color, passport):
#         super().__init__(name, weight, color)
#         self.passport = passport
#
#     def give_a_paw(self):
#         return f'I can give a paw is {self._name}'
#
#     def run(self):
#         return "I can run fast"
#
# dog3 = Pitbull('Lassie', 4, "black", "type1")
# print(dog3.run())
# print(dog2.run())
#
# print(dog2.set_name("Milka"))
# print(dog2.get_name())
# print(dog2.__dict__)
#
#
# class sports:
#     def __init__(self, acrobatics, __boxing, dancing):
#         self.acrobatics = acrobatics
#         self.__boxing = __boxing
#         self.dancing = dancing
#
#     def elisabet(self):
#         return f'I am good at {self.dancing}'
#
# experience_in = sports("few", 6, 3)
# print(experience_in.__dict__)


