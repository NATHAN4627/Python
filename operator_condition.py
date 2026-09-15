print("===Operators===")
# + -> >= <= % += -= ** //
# is not or and

a = 18
b = 4

res = a // b
res2 = a % b

print(res)
print(res2)


c = dict(name="Nathan", age=21)
d = dict(name="Nathan", age=21)

print(c == d)  # compares only value not references
print(c is d)


print("===Conditions===")
# x = 90

# if x > 50:
#     print("case A")
# elif x > 10:
#     print("case B")
# else:
#     print("case C")


age = 10

# Ternary operator (in Python there is no condition ? a : b)
person = "adult" if age > 18 else "child"
print(person)



is_student = False
is_admin = True

if not is_student:
    print("You are not student!")
elif is_admin:
    print("You are admin!")
else:
   print("else case")