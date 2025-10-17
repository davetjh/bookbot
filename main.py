import sys
from stats import count_words, count_letters, sort_dict

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    sorted_dict = sort_dict(count_letters(book))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
        else:
            continue
    print("============= END ===============")

main()