foods=['apples','cakes','beer','chips']

new_foods = foods[:]

foods.append('eggs')
new_foods.append('cheese')
print("The first 3 foods are")
for food in new_foods[-3:]:
	print(food)


winter = [value*10 for value in range(6)]
print(winter)