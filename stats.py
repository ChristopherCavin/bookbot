def number_of_words(bookstring):
    wordcount = 0
    for word in bookstring.split():
        wordcount += 1
    return wordcount

def number_of_characters(bookstring):
    bookstring = bookstring.lower()
    character_dictionary = {}
    for word in bookstring:
        for character in word:
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    return character_dictionary

def sorted_dictionary(unsorted):
    def sort_on(char):
        return char[1]
    sorted_dict = dict(
    sorted(unsorted.items(), key=sort_on, reverse=True)
    )
    return sorted_dict
