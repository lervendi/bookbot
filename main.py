
from stats import number_of_the_words

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text("books/frankenstein.txt") 
    num_words = number_of_the_words(book_text)
    print(f"{num_words} words found in the document")
main()

