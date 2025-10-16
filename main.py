from stats import count_words, count_letters

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    # count_words(get_book_text('books/frankenstein.txt'))
    print(count_letters(get_book_text('books/frankenstein.txt')))

main()