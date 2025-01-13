def main():
    file_name = "books/frankenstein.txt"
    text = get_book_text(file_name)
    words = count_words(text)
    letters = count_letters(text)
    print_report(file_name, words, letters)


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}
    
    lowered_text = text.lower()
    for c in lowered_text:
        if (c.isalpha()):
            if (c not in letters):
                letters[c] = 0
            letters[c] += 1

    return letters


def print_report(file_name, words, letters):
    sorted_letters = sort_letters(letters)
    print(f"--- Begin report of {file_name} ---")
    print(f"{words} words found in the document")
    print()
    for letter in sorted_letters:
        print(f"The '{letter["letter"]}' character was found {letter["value"]} times")

    print ("--- End report ---")


def sort_on(dict):
    return dict["value"]


def sort_letters(letters):
    list = []
    for l in letters:
        list.append({"letter": l, "value": letters[l]})
    list.sort(reverse=True, key=sort_on)
    return list 


def get_book_text(file_name):
    with open(file_name) as file:
        file_contents = file.read()
    return file_contents

main()
 