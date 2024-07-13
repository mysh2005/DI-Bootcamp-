import random

def get_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

def get_random_sentence(length, words):
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence

def main():
    print("This program generates a random sentence with a specified number of words.")
    
    try:
        length = int(input("Enter the length of the sentence (between 2 and 20): "))
        if length < 2 or length > 20:
            print("Error: The length must be between 2 and 20.")
            return
    except ValueError:
        print("Error: Please enter a valid integer.")
        return
    
    filename = '/Users/mysh/Desktop/DI_Bootcamp/Week 4/Day 4/Exercice XP/sowpods.txt' 
    words = get_words_from_file(filename)
    sentence = get_random_sentence(length, words)
    print(f"{sentence}")

if __name__ == "__main__":
    main()


    