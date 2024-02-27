
vogals = ['a', 'e', 'i', 'o', 'u']

def count_vogals(word):
    count = 0
    for letter in word:
        if letter in vogals:
            count += 1
    return count


print(f'The word has {count_vogals(input("Enter a word: "))} vogals')
