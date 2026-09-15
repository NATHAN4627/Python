print("===Operators===")
# + -> >= <= % += -= ** //
# is

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
