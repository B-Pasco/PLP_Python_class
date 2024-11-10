# Creating empty list in python
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

another_list = [50, 60, 70]
my_list.extend(another_list)

print(my_list)