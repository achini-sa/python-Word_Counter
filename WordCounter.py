import re

# welcome message
print("\n\nHello, Welcome to the word counter.\n\t\tEnter your text here to count words and numbers.")

# input
text = input("\nEnter your text here:\n\n")

def count_the_words(input_text):
    words = re.split(r'\W+', input_text)

    numbers = [word for word in words if word.isdigit()]
    words = [word for word in words if word.isalpha()]

    # word count
    word_count = len(words)
    print("Word count:", word_count)

    # number count
    number_count = len(numbers)
    print("Number count:", number_count)

    # count of words and count of numbers
    final_count = word_count + number_count
    print("Count of words and count of numbers:", final_count)

# run the application
count_the_words(text)
