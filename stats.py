def number_of_the_words(text):
    #split text by words
    words = text.split()
    #return the number of the words
    return len(words)

#what is the principle of sorting
def sort_on(items):
    return items["num"]

def sort_characters(char_dict):
    letters = []
    for char, num in char_dict.items():
        if char.isalpha():
            letters.append({"char": char, "num": num})
    
    letters.sort(reverse=True, key=sort_on)
    return letters



