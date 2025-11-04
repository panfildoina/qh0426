

#Asking user how many mountains to print?
mountains = int(input("How many mountains should I display?\n"))
print("Displaying...\n")

for i in range(mountains):
    print("""
              __
             /  \_
            /^    \
           /  ^    \_
         _/ ^ ^ ^    \
         / ^        ^ \
 """)
    
print()  # blank line between mountains

