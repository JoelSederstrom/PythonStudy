# 2022_01_18 Recommend using a simple code editor for python.  I used VisualStudioCode.  https://code.visualstudio.com/

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}
print('Items in the set "nearby_people" are: ' + str(nearby_people))

# Ask the user for the name of a friend
name_of_a_friend = input("Enter the name of a friend: ")
print("Name that was entered is: " + name_of_a_friend)

# Add the name to the empty set
user_friends.add(name_of_a_friend)
print('Items in the set "user_friends" are: ' + str(user_friends))

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print('This is a combination of both sets: ' + str(nearby_people.union(user_friends)))
print('This is what both sets have the same: ' + str(nearby_people.intersection(user_friends)))
print('These items are in nearby_people only: ' + str(nearby_people.difference(user_friends)))
print('These items are in name_of_a_friend only: ' + str(user_friends.difference(nearby_people)))
