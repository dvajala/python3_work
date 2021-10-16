unconfirmed = ['name1','name2','name3']
confirmed = []

unconfirmed = list(reversed(unconfirmed))

while unconfirmed:
    unconfirmed_user = unconfirmed.pop()
    print("confirming user " + unconfirmed_user.title())
    confirmed.append(unconfirmed_user)

print("The following users have been confirmed:")
for user in confirmed:
    print(user)
