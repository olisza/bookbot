def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    number_characters = count_characters(text)

    for c in number_characters:
        if c.isalpha():
            print(f"The '{c}' character was found {number_characters[c]} times")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(s):
    low_string = s.lower()
    char_count = {}
    for char in low_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


main()