#print("Bookbot is initializing")
from stats import number_of_words, number_of_characters, sorted_dictionary
import sys
def get_book_text(filepath):
    with open(filepath) as f:
        bookstring = f.read()
        return bookstring
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    wordcount_message = f"Found {number_of_words(get_book_text(filepath))} total words"
    #print(wordcount_message)
    Dictionary = number_of_characters(get_book_text(filepath))
    Dictionary_Message = ""
    for character in Dictionary:
        count = Dictionary[character]
        Dictionary_Message = Dictionary_Message + (f"'{character}': {count}, ")
   # print(Dictionary_Message)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(wordcount_message)
    print("--------- Character Count -------")
    Sorted_Dictionary = sorted_dictionary(Dictionary)
    for character in Sorted_Dictionary:
        count = Sorted_Dictionary[character]
        if character.isalpha():

            print(f"{character}: {count}")
    print("============= END ===============")
main()
