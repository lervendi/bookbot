import sys 
from stats import number_of_the_words, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def count_character(text):
    char_dict = {}
    for char in text:
        if char.isalpha() and char.isascii():
            char = char.lower()
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = number_of_the_words(book_text)
    char_list = count_character(book_text)
    sorted_list = sort_characters(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    print("DEBUG (first 10 symbols):", sorted_list[:10])

    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()


