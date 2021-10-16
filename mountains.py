reponses = {}

poll_active = True

while poll_active:
    name = input("Tell me your name: ")
    reponse = input("Which mountain would you like to climb?: ")

    reponses[name] = reponse

    repeat = input("Would you like someone else to take the poll? (yes/no): ")
    if repeat == 'no':
        poll_active = False

print("******* POLL RESULTS *******")
for name,response in reponses.items():
    print(f"{name.title()} would like to climb {response.title()}")