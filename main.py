import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    analysis_unparsed = char_analysis(text)
    list_letters = list(analysis_unparsed.keys())
    num_letters = list(analysis_unparsed.values())
    
    print(f"--- Beginning report of {book_path} ---\n")
    print(f"{num_words} words found in the document.\n")
    
    for i in range(len(num_letters)):
        print(f"The '{list_letters[i]}' character was found {num_letters[i]} times.")

    print(f"\n--- Ending report of {book_path} ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path, encoding='UTF-8') as f:
        return f.read()

def char_analysis(text):
    converted_text = text.lower()
    alphabet = string.ascii_lowercase
    return {letter: converted_text.count(letter) for letter in alphabet}

main()