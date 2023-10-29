car_list = ["BMW", "CAT", "JEEP"]
car_list.append("Ford")               #['BMW', 'CAT', 'JEEP', 'Ford']

l2 = list()
l2.append(3)
l2.append("computer")


print(car_list)
print(l2)

print(car_list[1])
print(car_list[-1])
print(car_list[-2])

#sorting in python mutable 
num = [1, 66, 77, 35, 57, 34, 76, 34]

# num.sort()  ######

print(num)

#sortiong in python immutable
shorted_num = sorted(num)

print(shorted_num)
