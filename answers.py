# 1. Create an empty list
my_list = []

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("List after appending elements:", my_list)
# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("List after inserting 15 at index 1:", my_list)

# 4. Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("List after extensions:", my_list)

# 5. Remove the last element
my_list.pop()
print("List after removing the last element:", my_list)

# 6. Sort in ascending order
my_list.sort()
print("List after sorting:", my_list)

# 7. Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Optional: Print the final list to see the result
print("Final list:", my_list)
