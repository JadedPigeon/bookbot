from stats import word_count, character_count, dictionary_sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



def main():
    book_text = get_book_text("books/frankenstein.txt")
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