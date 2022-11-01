# print in a function only for displaying some data
# when you return in a function you're going to use it again later in the program
from add_fruits import add_fruits
from subtract_fruits import subtract_fruits
from divide_fruits import divide_fruits
from display_fruits import display_fruits

apples=int(input("how many apples? "))
oranges=int(input("how many oranges? "))

# add fruits
# return value must be within variable
fruit_added= add_fruits(apples,oranges)
print(fruit_added)
# subtract fruits
fruit_subtracted= subtract_fruits(apples,oranges)
print(fruit_subtracted)

# # divide fruits
fruit_divided= divide_fruits(apples,oranges)
print(fruit_divided)
# display them all
display_fruits(fruit_added, fruit_subtracted, fruit_divided)

