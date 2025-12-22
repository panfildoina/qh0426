#P1 open a txt file  in read mode
try:
    file = open('my_text.txt', 'r')
    print("File opened successfully")
    #Remember to close the file
    file.close()
except FileNotFoundError:
    print("File not found.")

# P2 open a binary file named my_image.jpg in read mode
try:
    file = open('my_image.jpg', 'rb')
    print("File opened successfully")
    file.close()
except FileNotFoundError:
    print("File not found!")