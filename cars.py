# Now create another set of cars in a variable junkyard. 
# Someone who owns a junkyard full of old cars has 
# approached you about buying the entire inventory. 
# In the new set, add some different cars, 
# but also add a few that are the same 
# as in the showroom set.
# Use the intersection method to see which cars exist
# in both the showroom and that junkyard.
# Now you're ready to buy the cars in the junkyard.
# Use the union method to combine the 
# junkyard into your showroom.
# Use the discard() method to remove any
# cars that you acquired from the junkyard that
# you do not want in your showroom

showroom = set()
new_cars = {"Skyline", "GTR"}
junkyard = {"Chevy", "Hellcat", "Ford", "Ferarri", "GTR"}

showroom.update(["Hellcat", "Ferarri", "Corvette"])

showroom.update(new_cars)

# same_cars = showroom.intersection(junkyard)

all_cars = showroom.union(junkyard)

all_cars.discard("Ford")
all_cars.discard("Chevy")

print(all_cars)
# showroom.discard("Hellcat")
# print(len(showroom))
# showroom.add("Hellcat")
# print(showroom)