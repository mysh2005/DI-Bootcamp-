class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        self_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight
        if self_strength > other_strength:
            return f'{self.name} won the fight!'
        elif other_strength > self_strength:
            return f'{other_dog.name} won the fight!'
        else:
            return f'It was a draw!'

dog1 = Dog('Taxi', 4, 20)
dog2 = Dog('Zouzou', 5, 18)
dog3 = Dog('EKô', 5, 18)

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))

