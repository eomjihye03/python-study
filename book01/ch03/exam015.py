# if문

age = 30
if age < 20:
    print("teenager")
if age >= 20:
    print("adult")


age = 30
if age < 20:
    print("teenager")
else:
    print("adult")

age = 100
if age < 20:
    print("teenager")
elif age >= 20 and age < 65:
    print("adult")
else:
    print("old adult")

# python은 C, Java와 다르게 elif 존재.