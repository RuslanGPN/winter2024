# Lesson1
# task1_1
# x = int(input("value x = "))
# y = int(input("value y = "))
# print(f"Amount = {x+y}")
# print(f"Multiplication = {x*y}")

# # task1_2
# x = int(input("value x = "))
# y = int(input("value y = "))
# Amount = x + y
# Multip = x * y
# Subtraction = x - y
# print("Amount = ", Amount)
# print("Multip = ", Multip)
# print("Subtraction = ", Subtraction)
# if y==0:
#     print("zero divider, division isn't possible")
#     if Amount > Multip:
#         n1 = Amount
#     else:
#         n1 = Multip
#     if Subtraction > n1:
#         n1 = Subtraction
# else:
#     Division = float(x / y)
#     IntDivision = int(x // y)
#     print("Division = ", Division)
#     print("IntDivision = ", IntDivision)
#     if Amount > Multip:
#         n1 = Amount
#     else:
#         n1 = Multip
#     if Subtraction > n1:
#         n1 = Subtraction
#     if Division > n1:
#         n1 = Division
#     if IntDivision > n1:
#         n1 = IntDivision
# print(" ")
# print(f"Maximum value = {n1}")

# task1_3
x = int(input("value x = "))
y = int(input("value y = "))
Amount = int(x + y)
Multip = int(x * y)
Subtraction = int(x - y)
print("Amount = ", Amount)
print("Multip = ", Multip)
print("Subtraction = ", Subtraction)
if y == 0:
    print("zero divider, division isn't possible")
    if Amount >= Multip:
        n1 = Amount
        n2 = Multip
    else:
        n1 = Multip
        n2 = Amount
    if Subtraction > n2:
        n2 = Subtraction
    if Subtraction > n1:
        n2 = n1
        n1 = Subtraction
else:
    Division = float(x / y)
    IntDivision = int(x // y)
    print("Division = ", Division)
    print("IntDivision = ", IntDivision)
    if Amount > Multip:
        n1 = Amount
        n2 = Multip
    else:
        n1 = Multip
        n2 = Amount
    if Subtraction > n2:
        n2 = Subtraction
    if Subtraction > n1:
        n2 = n1
        n1 = Subtraction
    if Division > n2:
        n2 = Division
    if Division > n1:
        n2 = n1
        n1 = Division
    if IntDivision > n2:
        n2 = IntDivision
    if IntDivision > n1:
        n2 = n1
        n1 = IntDivision

print(" ")
print(f"Maximum value = {n1}")
print(f"Second value = {n2}")
