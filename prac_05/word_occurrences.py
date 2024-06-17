# text = "this is a collection of words of nice words this is a fun thing it is"

text = input("Enter Text: ")

words = sorted(text.split(" "))

words_dictionary = {}

for word in words:
    words_dictionary[word] = 0
    for compare_word in words:
        if compare_word == word:
            words_dictionary[word] += 1

longest_word_length = max({len(each_word) for each_word in words_dictionary.keys()})

for word in words_dictionary.keys():
    print(f"{word:{longest_word_length + 2}}: {words_dictionary[word]}")