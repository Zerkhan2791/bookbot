import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = len(text.split())
    analysis_unparsed = char_analysis(text)
    
    print(f"--- Beginning report of {book_path} ---\n")
    print(f"{num_words} words found in the document.\n")
    
    for letter, nb in analysis_unparsed.items():
        print(f"The '{letter}' character was found {nb} times.")

    print(f"\n--- Ending report of {book_path} ---")

def get_book_text(path):
    with open(path, encoding='UTF-8') as f:
        return f.read()

def char_analysis(text):
    converted_text = text.lower()
    alphabet = string.ascii_lowercase
    return {letter: converted_text.count(letter) for letter in alphabet}

main()