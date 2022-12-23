class Person:
    number_of_people = 0
    # Gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person("tim")
print(Person.number_of_people)
p2 = Person("jill")
print(Person.number_of_people)

# print(p1.number_of_people)
# print(Person.number_of_people)

# Person.number_of_people = 8
# print(p2.number_of_people)
# Person.number_of_people = 9
# print(p1.number_of_people)
