def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


starting = 0
even_number = list()

# while starting <= 100:
#     if is_even(starting):
#         even_number.append(starting)
#         print(f"{starting} is Even")
#     else:
#         print(f"{starting} is Odd")
#     starting += 1

for value in range(0, 100 + 1):
    if is_even(value):
        even_number.append(value)
        print(f"{value} is Even")
    else:
        print(f"{value} is Odd")


print(even_number)