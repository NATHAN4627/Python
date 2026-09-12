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
    #@staticmethod => if (cls) no need
    def about(cls):
        print("static method property executed!")


# ordinary state
person = Person("Kevin", 21)
person.introduce()
person.sayAge()


# static state
print(Person.message)

#static method
Person.about()
