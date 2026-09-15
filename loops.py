import random

text = "Nathan"
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rang_obj = range(3)
person_obj = dict(name="Kevin", age=21)

for letter in text:
    print(letter)
print("--------")
for num in nums:
    print(num)
print("--------")
for range in rang_obj:
    print(range)
print("--------")
for key in person_obj:
    print(f"key: {key}, value: {person_obj.get(key)}")

print("===break/else===")
for num in nums:
    print(num)
    if num > 5:
        break
else:
    print("Looped successfully")


print("===while===")
res = random.randint(1, 10)
count = 0

while True:
    count += 1
    myRes = int(input("Find number to match: "))

    if res == myRes:
        print(f"You found number in {count} steps!")
        break
    else:
        print("try again!")
