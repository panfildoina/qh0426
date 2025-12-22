#Creating a module  named file_operations 
#creating a fuction to write text to a file
def write_to_file(filename, content):
    with open(filename,'w') as f:
        f.write(content)

#creating a function to read text to a file
def read_from_file(filename):
    with open(filename, 'r') as f:
        return f.read()
    
