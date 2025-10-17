def count_words(book_str):
    word_list = book_str.split()
    return len(word_list)

def count_letters(book_str):
    letter_dict = {}
    for char in book_str:
        letter = char.lower()
        if letter in letter_dict:
                letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

# helper function for sort_dict function
def sort_on(dict):
     return dict["num"]

def sort_dict(dict):
    list_dict = []
    for pair in dict:
        list_dict.append({"char": pair, "num": dict[pair]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict