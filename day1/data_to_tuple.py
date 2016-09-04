data = input("Enter your numbers separated by a comma and a trailing space [eg) 5, 6, 7]: ")
array = data.split(", ")
immutable = tuple(array)

print("List: {}".format(array))
print("Tuple: {}".format(immutable))
