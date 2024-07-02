class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat('Snow', 4)
cat2 = Cat('Lili', 6)
cat3 = Cat('Minou', 2)

def find_oldest_cat(*cats):
    oldest_cat = max(cats, key=lambda cat: cat.age)
    return oldest_cat

oldest_cat = find_oldest_cat(cat1, cat2, cat3)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")