#1. DICTIONAY - creating a dictonary with 5 key-value pairs
my_dict = {'name': 'Doina', 'country': 'United Kingdom', 'age': 31, 
           'nationality': 'romanian', 'marital status': 'married'}

#Adding a new pair
my_dict ['hobby'] = 'yoga'

#updating an existing pair
my_dict ['country']  = 'Moldova'
#deleting a pair 

del my_dict ['marital status'] 

print(my_dict)

#2. SET OPERATIONS - creating two sets  
my_set1 = {2, 6, 9, 3, 12, 5}
my_set2 = {6, 4, 5, 11}

#  perform union
print("Union:", my_set1.union(my_set2))

# intersection 
print("Intersection:", my_set1.intersection(my_set2))

# difference
print("Difference:", my_set1.difference(my_set2))

#and symmetric difference operation
print("Symetric Difference:", my_set1.symmetric_difference(my_set2))

#3. Tuples Creation and Concatenation
#Creating two tuples
my_tuple1 = (3, 5, 9, 6, 5)
my_tuple2 = (2, 6, 8)

#concatenating tuples
new_tuple = my_tuple1 + my_tuple2
print("Concatenated tuple:", new_tuple)

#finding the index of an element
index = new_tuple.index(5)
print("Index of 5:", index)

#create a nested tuple
nested_tuple = (1, (4, 5), 3)

#Access the inner_tuple
inner_tuple = nested_tuple[1]
print("Inner Tuple:", inner_tuple)   