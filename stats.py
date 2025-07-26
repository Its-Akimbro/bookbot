def get_count_words_of_book(book_contents):
    list_of_book_contents = book_contents.replace("\n", " ").split(' ')
    count = 0
    for i in enumerate(list_of_book_contents):
        if i[1] == '':
            continue
        count += 1
    return count

def get_count_letters_in_book(book_contents):
    dict_of_letters = {}
    for i in book_contents.lower():
        if i not in dict_of_letters:
            dict_of_letters[i] = 1
        else:
            dict_of_letters[i] += 1
    return dict_of_letters

def sort_dict_of_letters(dict_of_letters):
    list_of_letters = []
    
    for i in dict_of_letters.items():
        list_of_letters.append({"char":i[0], "num":i[1]})

    list_of_letters.sort(reverse=True, key=lambda letter: letter["num"])
    
    return list_of_letters
    