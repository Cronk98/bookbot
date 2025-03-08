from stats import get_word_count
from stats import get_char_count
from stats import sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print ("Usage: python3 main.py <path_to_book>")

    else:
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
        word_count = get_word_count(book_text)

        print("============ BOOKBOT ============\n"
              f"Analyzing book found at {file_path}...\n"
              "----------- Word Count ----------")
    
        print(f"Found {word_count} total words")

        print("--------- Character Count -------")

        char_dict = get_char_count(book_text)
        sorted_dict = sort_dict(char_dict)
        for pair in sorted_dict:
            if pair["char"].isalpha() == True:
                print(f"{pair["char"]}: {pair["count"]}")

        print("============= END ===============")



main()