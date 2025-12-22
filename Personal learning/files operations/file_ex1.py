#open the text file
file = open('my_text_file.txt', 'r')

#Read the first line 
first_line = file.readline()

#print the type of the object returned
print(type(first_line))

#close the file

file.close()
