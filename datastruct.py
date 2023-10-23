# LIST - collection of ordered, indexed, changeable elements which can be of different data types
numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

for num in numbers:
    print(num)  # looping over a list

print(numbers[0])  # Accessing the first element
print(numbers[-1])  # Accessing the last element
print(numbers[1:4])  # Accessing elements within that range

numbers.sort()
numbers[0] = "Python"  # Changing the value of first element
numbers.append("kiwi")
print(numbers)

# TUPLES - just like lists, but are immutable i.e. its values cannot be changed once initiated
a = (1, 2, 3, 4, [2, 3])
for item in a:
    print(item)
# indexing is similar to lists
print(a[0])
print(a[-1])
print(a[0:])
a.count(2)
# a[0] = 9 #Raises an exception


# SETS - just like tuples but cannot contain duplicate elements and they are unordered
st = {1, 2, 2, 23.4}  # Removes all duplicated
print(st)
st.add(5)
st.remove(23.4)
print(st)
print(len(st))

# DICTIONARIES - they are of the form of key-value pairs, are ordered and its elements can be changed but
# cannot contain duplicate elements
person = {"name": "John", "age": 20, "skill": "Coding"}
print(f"{person['name']} is {person['age']} years old and is really skilled in {person['skill']}")
# Adding elements in a dict
person["gender"] = "male"
print(person)
