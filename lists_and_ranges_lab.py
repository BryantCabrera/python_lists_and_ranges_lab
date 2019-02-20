"""
Exercise 1
Create a list named students containing some student names (strings).
Print out the second student's name.
Print out the last student's name.
"""
students = ['Bryant', 'Michael', 'Kevin', 'Brent', 'Peter', 'Abe', 'Ummer']
print(students[1])
print(students[-1])


"""
Exercise 2
Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
Use a for loop to print out the string "food goes here is a good food"
"""
foods = ('Korean BBQ', 'tacos', 'steak', 'burrito', 'pho', 'korean BBQ 2', 'cheese fries')

for food in foods:
    print(food + ' is a good food.')


"""
Exercise 3
Using a for loop, print just the last two food strings from foods.
"""
for i in range (len(foods)-2, len(foods)):
    print(foods[i])