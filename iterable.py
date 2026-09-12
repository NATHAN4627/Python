print("===Iterable objects===")

# for letter in "NATHAN":
#     print(f"letter: {letter}")


# range_obj = range(9)
# print("range result:", range_obj)

# for ele in range_obj:
#     print(f"result of range: {ele}")


print("===Dictionary===")
# person_obj = {"name": "Nodirjon", "age": 21, "married": False}
# print(person_obj)
person_dict = dict(name="Nodirjon", age=21, married=False)  # => most used
print(person_dict)

person_name = person_dict["name"]
print(person_name)

for value in person_dict.values():
    print(f"value: {value}")


for keys in person_dict.keys():
    print(f"key: {keys}")
