print("DEFINE AND CALL")

# Define(param)


def greet(n):
    print(f"How do you do {n}?")


def getAge(a):
    return f"You are {a} years old"


# Call(arg)
greet("NATHAN")
res = getAge(21)
print(res)


print("Keyword & default args")


def getInfo(name, age):
    return f"Hi {name}! You are {age} years old"


res1 = getInfo(name="Kevin", age=24)
print(res1)


print("Scope")

b = 20  # 3


def calculate(a):  # 2
    c = a + b  # 1
    print("c = ", c)


calculate(10)
