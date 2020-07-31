import requests, os.path, operator

path = "./challenges/03/03-src/assets/quijote.txt"
url = "http://www.gutenberg.org/cache/epub/2000/pg2000.txt"

def open_file ():    
    if os.path.isfile(path) == False:    
        myFile = requests.get(url)
        open(path, "wb").write(myFile.content)
        myFile.close()
    return open(path, "r", encoding = "utf8")    

def take_only_book_text(file, start_line, end_line):
    line = file.readline()
    start = 0
    end = 0
    content = ""
    
    while line:        
        if line.startswith(start_line):
            start = file.tell()-1
        elif line.startswith(end_line):
            end = file.tell()
            
        if start != 0 and end != 0: 
            break
        line = file.readline()
    
    file.seek(start)      
    line = file.readline()

    while line:
        if file.tell() == end:
            break
        else:
            content += line 
        line = file.readline()
    return content.strip()

def count_words(words_list):
    dict_words = {}
    words = words_list.split()
    
    for word in words:
        dict_words[word] = dict_words.setdefault(word, 0) + 1

    return dict_words  

def count_vowles(words_list):
    dict_vowles = {}
    
    for word in words_list:
        for letter in word:
            if letter == "a" or letter == "e" or  letter == "i" or letter == "o" or  letter == "u":
                dict_vowles[letter] = dict_vowles.setdefault(letter, 0) + 1

    return dict_vowles

def count_word(words_list, word_to_count):
    return words_list.split().count(word_to_count)

def print_result(word_dict, max_results, order):
    results = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = order)
    count = max_results
    
    for result in results:
        if count != 0: 
            print(result)
            count -= 1
        else:
            print("\n")
            break

def count_unique_words(word_dict):
    count = 0
    
    for result in word_dict.items():
        if result[1] == 1:
            count += 1
    return count



content = take_only_book_text(open_file(), "file corrections and new HTML file by Joaquin Cuenca Abela.", "End of")
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
