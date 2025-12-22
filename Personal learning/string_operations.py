#creating a  module string_operations.py 
#creating a function to reverse the word 
def reverse_string(s):
    return s[::-1]

#to capitalize the first letter of each word in a string
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
