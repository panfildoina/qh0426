with open('exercise1.txt', 'w') as file:
    file.write("Hello, this is Exercise 1.")

#exercise 2 - open a file, read its content and the close it 
#then try reading from the file again after you've closed it

#open the file in read mode
with open('exercise1.txt', 'r') as file:
    content = file.read()
    print("Content before closing: : ", content)
#try to read the file after closing
try:
    print("Trying to read after closing: ", file.read())
except ValueError as e:
    print(f"An error occurred: {e}") 