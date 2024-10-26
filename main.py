global_letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print_report(book_path, word_count, letter_count)

def print_report(book_path, word_count, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print (f"{word_count} words found in the document\n")
    for key in letter_count:
        print(f"The '{key}' character was found {letter_count[key]} times")
    print("--- End report ---")

def get_letter_count(text):
    letter_count = {}
    for character in text.lower():
        if character in global_letters:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1
    letter_count = dict(sorted(letter_count.items(), key=lambda x:x[1], reverse=True))
    return letter_count

def get_word_count(text):
    word_list = text.split()
    return len(word_list)

def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text

main()