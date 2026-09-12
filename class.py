class Person():

    # static state
    message = "static state property"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}")

    def sayAge(self):
        print(f"I am {self.age} years old!")

    @classmethod
    # @staticmethod => if (cls) no need
    def about(cls):
        print("static method property executed!")


# ordinary state
# person = Person("Kevin", 21)
# person.introduce()
# person.sayAge()


# # static state
# print(Person.message)

# #static method
# Person.about()


print("===special methods===")


class Car():
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def startEngine(self):
        print(f"{self.name} started engine")

    def stopEngine(self):
        print(f"{self.name} stopped engine")

    def __str__(self):
        return f"Car name {self.name}, produced in {self.year}"

    def __call__(self):
        print("Object method called")


car = Car("Urus", 2025)
car.startEngine()
car.stopEngine()
print(car)
car()
