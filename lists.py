motorcycles = []

motorcycles.append('honda')
motorcycles.append('enfield')
motorcycles.append('yamaha')
motorcycles.append('ducati')

print(motorcycles)

popped_motorcyle = motorcycles.pop(0)

print(motorcycles)
print(popped_motorcyle)

guest_list = ['first','second','third']

guest_list[0] = 'new first'

guest_list.insert(0,'new new first')
guest_list.insert(2,'middle')
guest_list.append('new last')

print("welcome to dinner " + guest_list[0])
print(guest_list)

print("sorry no dinner " + guest_list.pop())
print(guest_list)
print("sorry no dinner " + guest_list.pop())
print(guest_list)
print("sorry no dinner " + guest_list.pop())
print(guest_list)
print("sorry no dinner " + guest_list.pop())
print(guest_list)

del guest_list[1]
print(guest_list)
del guest_list[0]
print(guest_list)
