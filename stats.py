def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(filepath):
    wc = 0
    text = get_book_text(filepath)
    words = text.split()
    for word in words:
        wc += 1
    return wc


def get_char_count(filepath):
    letter_dict = {}
    text = get_book_text(filepath)
    text = text.lower()
    words = text.split()
    for word in words:
        for letters in word:
            if letters in letter_dict:
                letter_dict[letters] += 1
            else:
                letter_dict[letters] = 1
    return letter_dict


def letter_organizer(filepath):
    dict = get_char_count(filepath)
    dict_items = list(dict.items())
    sorted_items = sorted(dict_items, key=lambda x: x[1], reverse=True)
    for letter, count in sorted_items:
        print(f"{letter}: {count}")


def book_analysis(filepath):
    print("=========BookBot============")
    print(f"\nAnalyzing book found at {filepath}\n")
    print("--------Word Count---------")
    word_count = get_num_words(filepath)
    print(f"\nFound {word_count} total words\n")
    print("------Character Count------")
    letter_organizer(filepath)
