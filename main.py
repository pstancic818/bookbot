from stats import get_word_count, get_character_count, sort_character_count
import sys

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        filepath (str): The path to the book file.
        
    Returns:
        str: The content of the book file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Book file not found."
    except Exception as e:
        return f"An error occurred: {e}"
def main():
    book = sys.argv[1]
    text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print("Found " + str(get_word_count(text)) + " total words")
    print("--------- Character Count -------")
    text_dict = get_character_count(text)
    text_dict = sort_character_count(text_dict)
    for i in text_dict:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['count']}")
        else:
            continue
if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()