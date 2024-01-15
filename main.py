def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = char_analysis(text)
    print(f"{num_words} words found in the document")
    print(f"{num_letters} found.")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_analysis(text):
    converted_text = text.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    character_totals = {}
    for letter in alphabet:
        char_count = converted_text.count(letter)
        character_totals[letter] = char_count
    return character_totals

main()