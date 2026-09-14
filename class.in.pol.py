print("===Inheritance===")


class Animal:  # (object) by default
    description = "This class is parent"

    def __init__(self, voice):
        self._voice = voice

    def makeVoice(self):
        print("This animal makes voice:", self._voice)


class Dog(Animal):
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def makeVoice(self):
        print(f"This {self.name} makes voice: {self._voice}")


class Fish(Animal):
    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")


dog = Dog("Alfa", "vov", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
dog.makeVoice()
fish.introduce()
fish.makeVoice()

print(dog._voice)


print("===Polymorphism===")

dog.makeVoice()

# object-subClass-parentClass-objectClass

a = isinstance(fish, Fish)
b = isinstance(dog, Animal)
print(a, b)
