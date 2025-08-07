from stats import count_words, count_all_characters, sort_character_counts
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    word_count = count_words(get_book_text(book_path))
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_counts = count_all_characters(get_book_text(book_path))
    sorted_counts = sort_character_counts(character_counts)
    for character in sorted_counts:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")

    print("============= END ===============")


main()
