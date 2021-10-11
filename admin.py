new_names = ['Veda','Dinesh','admin','anu','john']
current_names = ['veda','dinesh','admin','tim','jack','jimmy']
if new_names:
    for name in new_names:
        if name.lower() in current_names:
            print(f"{name.title()} is already taken, please create a new name")
        elif name == 'admin':
            print (f"Hello {name.title()}, would you like to see a status report?")
        else:
            print (f"Hello {name.title()}, thank you for logging in")
else:
    print(" No users to greet")    