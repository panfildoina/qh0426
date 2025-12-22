import file_operations

#write content to a file
file_operations.write_to_file('sample.txt', 'Hello, world!')

#Read content from a file 
print(file_operations.read_from_file('sample.txt'))
