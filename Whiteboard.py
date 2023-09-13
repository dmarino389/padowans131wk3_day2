string = input('Enter a string: ')
vowels = ['a', 'e', 'i', 'o', 'u']

def count_vowels(string):
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

num_vowels = count_vowels(string)
print(f'The number of vowels in the string is: {num_vowels}')
