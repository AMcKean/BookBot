from stats import book_analysis


def main():
    path_to_book = "./books/frankenstein.txt"

    analysis = book_analysis(path_to_book)
    print(analysis)


main()
