import os.path
import requests
import operator


def open_file (path, url): 
    ''' Función que retorna un fichero. Si existir el fichero en la ruta indicada lo abre, 
    si no lo descarga y guarda dicha ruta.'''

    if os.path.isfile(path) == False:           # Controlo que no existe el fichero en la ruta
        myFile = requests.get(url)              # Lo descarga de la url indicada                    
        open(path, "wb").write(myFile.content)  # Creo un fichero nuevo, vuelco los datos descargados
        myFile.close()                          # Lo cierro
    return open(path, "r", encoding = "utf8")   # Lo abro de nuevo, pero en modo lectura y codificado en utf8 

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

