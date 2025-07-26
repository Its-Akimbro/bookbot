import sys

from stats import get_count_words_of_book
from stats import get_count_letters_in_book
from stats import sort_dict_of_letters

def get_book_contents(program_director):
    with open(f"{program_director}") as book:
        book_contents = book.read()
    return book_contents

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    program_director = sys.argv[1]
    book = "frankenstein.txt"
    book_contents = get_book_contents(program_director)    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}...")
    print(f"Found {get_count_words_of_book(book_contents)} total words")
    print(f"--------- Character Count -------")

    for i in sort_dict_of_letters(get_count_letters_in_book(book_contents)):
        if i['char'].isalpha():
            print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")


main()