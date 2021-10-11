available_toppings = ['mushrooms','olives','green peppers','extra cheese',
                        'pepperoni','pineapple']
requested_toppings = ['mushrooms','french fries','extra cheese']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we dont have {requested_topping}.")
else:
    print("Are you sure you want a plain Pizza?")
print("\nFinished making your pizza!")