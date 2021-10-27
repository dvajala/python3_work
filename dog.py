class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is sitting")
    def roll_over(self):
        print(f"{self.name} rolled over")


my_dog = Dog('timmy',3)
print(my_dog.name,my_dog.age)
my_dog.sit()
my_dog.roll_over()