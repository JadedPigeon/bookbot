from stats import word_count, character_count, dictionary_sort
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    words = word_count(book_text)
    book_characters = character_count(book_text)
    sorted_character_counts = dictionary_sort(book_characters)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_character_counts:
        if item["character"].isalpha():
            print(f"{item["character"]}: {item["count"]}")




main()