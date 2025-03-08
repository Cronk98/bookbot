from stats import get_word_count
from stats import get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "./books/frankenstein.txt"
    book_text = get_book_text(file_path)
    get_word_count(book_text)
    get_char_count(book_text)

main()