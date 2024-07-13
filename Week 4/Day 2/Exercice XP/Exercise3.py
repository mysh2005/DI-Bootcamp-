import random
import string

def generate_random_string(length=5):
    letters = string.ascii_letters  
    return ''.join(random.choice(letters) for _ in range(length))

if __name__ == "__main__":
    random_str = generate_random_string()
    print(f"Random String of length 5: {random_str}")
