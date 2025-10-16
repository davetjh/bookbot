def count_words(book_str):
    word_list = book_str.split()
    print(f"Found {len(word_list)} total words")

def count_letters(book_str):
    letter_dict = {}

    for char in book_str:
        letter = char.lower()
        if letter in letter_dict:
                letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    return letter_dict