from functions import *

path = "./challenges/03/03-src/assets/quijote.txt"
url = "http://www.gutenberg.org/cache/epub/2000/pg2000.txt"


content = take_only_book_text(open_file(path, url), "file corrections and new HTML file by Joaquin Cuenca Abela.", "End of")
words_list = content.replace("\n", " ").replace(".", " ").replace(",", " ").replace("?", " ").replace("¿", " ").replace(":", " ")
word_dict = count_words(words_list)

print(len(words_list), "words found \n")
print(count_unique_words(word_dict), "unique words found \n")
print(count_vowles(words_list ), "vowels found \n")
print(count_word(words_list, "Quijote"), "appearances of 'Quijote' \n")
print(count_word(words_list, "quijote"), "appearances of 'quijote' \n")

print("The 100 words more repeating are:")
print_result(word_dict, 100, True)
print("The 100 words less repeating are:")
print_result(word_dict, 100, False)
