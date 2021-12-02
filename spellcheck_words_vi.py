dictionary = set()

def read_dictionary_file():
    global dictionary
    if dictionary:
        return

    with open("tiengvietok123.txt", "r", encoding="utf8") as f:
        contents = f.read()

    dictionary = set(
        word.lower()
        for word in contents.splitlines()
    )

def is_spelled_correctly_vi(word):
    # Return True if spelled correctly; false otherwise
    word = word.lower()
    read_dictionary_file()
    return word in dictionary


