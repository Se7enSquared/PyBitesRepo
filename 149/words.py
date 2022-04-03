def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    words.sort()
    for i in range(len(words)):
        if words[i][0].isalpha():
            number_list = words[:i]
            word_list = words[i:]
            break
    return sorted(word_list, key=str.casefold) + sorted(number_list)

