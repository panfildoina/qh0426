
#open the text fuke
file = open('my_text_file.txt', 'r')

#return the first line
first_line = file.readline()

#Print the type of object returned
print(type(first_line))

#close the file
file.close()