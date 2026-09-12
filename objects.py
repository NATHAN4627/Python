import math
from math import ceil

# print("===Objects===")
# # Object has state and method properties

# res = math.ceil(95.2)
# print("res = ",res)

# res2 = ceil(93.8)
# print("res2 = ",res2)


print("===Error handling system===")

car_dict = dict(name="Tayota", year=2026, elevtric=True)

try:
    res = car_dict["origin"]
    print("res : ", res)
except Exception as err:   # Exception is universal for any type of errors
    print("No origin key found", err)
else:
    print("Executed without errors")
finally:
    print("Final logic here")
