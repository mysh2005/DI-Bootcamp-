class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

davids_dog = Dog(name="Rex", height=50)

print(f"David's dog: Name - {davids_dog.name}, Height - {davids_dog.height} cm")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog(name="Teacup", height=20)

print(f"Sarah's dog: Name - {sarahs_dog.name}, Height - {sarahs_dog.height} cm")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)
