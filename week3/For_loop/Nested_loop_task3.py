user = int(input("Please enter a sequence:\n"))

marker = input("Please eneter the character for the marker:\n")

marker1 = -1
marker2 = -1

for position in range(0, len(user), 1):
    letter = user[position]
  
    if letter == marker:
        if(marker1 == -1):
            marker1 = position
        else:
            marker2 = position 

print(f"The distance between the marker is {marker2 -marker1 -1}.")