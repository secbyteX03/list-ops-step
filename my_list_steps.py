# Step 1: create an empty list
my_list = []
print("my_list:", my_list)

# Step 2: append 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("after appends:", my_list)

# Step 3: insert 15 at second position (index 1)
my_list.insert(1, 15)
print("after inserting 15 at index 1:", my_list)

# Step 4: extend with [50, 60, 70]
my_list.extend([50, 60, 70])
print("after extending with [50, 60, 70]:", my_list)

# Step 5: remove last element
removed = my_list.pop()  # pops last element
print("removed last element:", removed)
print("current list:", my_list)

# Step 6: sort list ascending
my_list.sort()
print("after sorting ascending:", my_list)