class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family")
    
    def is_18(self, member_name):
        for member in self.members:
            if member['name'] == member_name:
                return member['age'] >= 18
        return False
    
    def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(f"  Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Child: {member['is_child']}")

initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

family_instance = Family(last_name="Johnson", members=initial_members)

print(f"Is Michael over 18? {family_instance.is_18('Michael')}")
print(f"Is Sarah over 18? {family_instance.is_18('Sarah')}")
family_instance.family_presentation()
