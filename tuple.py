print("===Tuple===")

# ==== tuple vs list ====

# Pythonda odatda kuproq list ishlatiladi arrayga qaraganda chunki arraylar katta sonlar ustida ishlaganda ishlatamiz.
# Array larninig barchasi aslida list hisoblanadi

# literal
nums = [1, 2, 3, 4, 5]
car_obj = {"brand": "BMW", "year": 1995}

# constructor
letters = list("Hello World")

# Tuple () qavs orqali yaratiladi va ularni yaratgandan keyin uzgartirib bulmaydi va bu xavfsizlik uchun yaxshi, Va kam xotirada joy egallaydi.

fruits = ("banana", "kiwi", "cherry")  # tuple
print(fruits)
# fruits[1] = "melon" cannot change

print("===Unpacking args===")
cities = ["Tashkent", "Jizzakh", "Navoiy", "Fergana"]
# *z qilib qolgan qiymatlarni bitta listga solib olib berepti
# Tuple orqali lsitdagi argumentlani unpack qilib olepiz
(x, y, *z) = cities
print(f"x = {x}, y = {y}")
print(f"z = {z}")


# *args > tuple
def calculate(*args):
    print("*args > ", args)
    total = 1
    for x in args:
        total *= x
    print("total value: ", total)
    return total


calculate(1, 2, 3, 4)
print("-----")
calculate(5, 6, 2)
