from stats import get_num_words, get_num_char, sort_dict
import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_char(text)
    chars_sorted = sort_dict(chars_dict)
    print_report(book_path, num_words, chars_sorted)




def print_report(book_path, num_words, chars_sorted):
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book_path}")

    #function 2
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #function 3
    print("--------- Character Count -------")
    #function 4
    for each in chars_sorted:
        print(f"{each['char']}: {each['num']}")






if __name__ == "__main__":
    main()
