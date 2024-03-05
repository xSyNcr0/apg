# APG v 1.0
# Advanced password generator
#
# by xSyNcr0
import time

develop = True
base_wordlist = set()
passwords = set()
min_char = 8
max_char = 12
password_options = {"min_char": 8, "max_char": 12, "contains_uppercase": False, "contains_lowercase": True, "contains_special_chars": True, "contains_numbers": True}
special_chars = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '\\', '?', '~'}

def pusher(array, data):
    if isinstance(data, set):
        for element in data:
            array.add(element)
    elif isinstance(data, list):
        for element in data:
            array.append(element)
    else:
        array.add(data)

def toBaseWL(data):
    pusher(base_wordlist, data)

def toPsw(data):
    pusher(passwords, data)

def reverse(text):
    if isinstance(text, (set, list)):
        base = set()
        for element in text:
            base.add(reverse(element))
        return base
    elif isinstance(text, int):
        text = str(text)
        
    elif isinstance(text, str):
        return text[::-1]
    return ""

def decodeDate(input):
    base = set()
    for element in input:
        base.add(strRemover(input, '-'))
    return base

def strRemover(text, char):
    return text.replace(char, "")

def toUpper(input):
    base = set()
    for element in input:
        tmp = generateUpperCombinations(element)
        for x in tmp:
            base.add(x)
    return base

def generateUpperCombinations(input_string):
    input_string = input_string.lower()
    result = set()

    for i in range(2**len(input_string)):
        modified_string = list(input_string)
        for j in range(len(input_string)):
            if (i >> j) & 1:
                modified_string[j] = modified_string[j].upper()
        result.add(''.join(modified_string))
    return result

def inputCleaner(input_string):
    base = set()
    elements = input_string.split(",")
    for element in elements:
        base.add(element.lower().strip())
    return base

def save(content):
    file = open("wordlist.txt", "w")
    for row in content:
        file.write(row + '\n')
    file.close()

def simpleComposer(set_1, set_2):
    base = set()
    for element in set_1:
        for second_element in set_2:
            base.add(str(element) + str(second_element))
    return base

def removeVocals(input):
    if isinstance(input, set):
        base = set()
        for element in input:
            base.add(removeVocals(element))
        return base
    elif isinstance(input, str):
        return input.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

def removeConsonants(input_data):
    if isinstance(input_data, set):
        result_set = set()
        for element in input_data:
            result_set.update(removeConsonants(element))
        return result_set
    elif isinstance(input_data, list):
        result_list = []
        for element in input_data:
            result_list.extend(removeConsonants(element))
        return result_list
    elif isinstance(input_data, str):
        return ''.join(char for char in input_data if char.lower() in 'aeiou')
    else:
        return input_data

def passwordsCleaner():
    global passwords
    base = set()
    for password in passwords:
        if (len(password) < password_options["min_char"]) or (len(password) > password_options["max_char"]):
            continue

        if password_options["contains_uppercase"]:
            if not any(char.isupper() for char in password):
                continue

        if password_options["contains_lowercase"]:
            if not any(char.islower() for char in password):
                continue
        
        if password_options["contains_special_chars"]:
            if not any(char in special_chars for char in password):
                continue
        
        if password_options["contains_numbers"]:
            if not any(char.isdigit() for char in password):
                continue

        base.add(password)
    passwords = sorted(base, key=lambda x: (len(x), x.lower()))

def wordsSplitter(input):
    if isinstance(input, (set, list)):
        base = set()
        for element in input:
            pusher(base, wordsSplitter(element))
        return base
    elif isinstance(input, str):
        result_set = set()
        n = len(input)

        for i in range(1 << n):
            combination = [input[j] for j in range(n) if (i >> j) & 1]
            result_set.add(''.join(combination))

        return result_set

def wordSplitterCombinations(input_string):
    result_set = set()
    n = len(input_string)

    # Genera tutte le possibili combinazioni di caratteri
    for i in range(1 << n):
        combination = [input_string[j] for j in range(n) if (i >> j) & 1]
        result_set.add(''.join(combination))

    # Aggiungi combinazioni di lunghezza 0 a n
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            combination = input_string[start:start + length]
            result_set.add(combination)

    return result_set

def obfuscatedChar(input):
    if isinstance(input, set):
        base = set()
        for element in input:
            base.add(obfuscatedChar(element))
        return base
    elif isinstance(input, str):
        return mapperObfucatedChar(input)

def mapperObfucatedChar(string):
    result_set = set()
    for i in range(len(string)):
        current_char = string[i]        
        if current_char.lower() == 'a':
            result_set.add(string[:i] + '@' + string[i+1:])
            result_set.add(string[:i] + '4' + string[i+1:])
        elif current_char.lower() == 'b':
            result_set.add(string[:i] + '8' + string[i+1:])
        elif current_char.lower() == 'c':
            result_set.add(string[:i] + '(' + string[i+1:])
            result_set.add(string[:i] + '{' + string[i+1:])
        elif current_char.lower() == 'e':
            result_set.add(string[:i] + '3' + string[i+1:])
        elif current_char.lower() == 'g':
            result_set.add(string[:i] + '9' + string[i+1:])
        elif current_char.lower() == 'i':
            result_set.add(string[:i] + '!' + string[i+1:])
            result_set.add(string[:i] + '1' + string[i+1:])
        elif current_char.lower() == 'l':
            result_set.add(string[:i] + '|' + string[i+1:])
            result_set.add(string[:i] + '1' + string[i+1:])
        elif current_char.lower() == 'o':
            result_set.add(string[:i] + '0' + string[i+1:])
        elif current_char.lower() == 's':
            result_set.add(string[:i] + '$' + string[i+1:])
            result_set.add(string[:i] + '5' + string[i+1:])
        elif current_char.lower() == 't':
            result_set.add(string[:i] + '7' + string[i+1:])
            result_set.add(string[:i] + '+' + string[i+1:])
    return result_set


def main():
    print("APG v1.0 by xSyNcr0")

    # input stage
    words = inputCleaner("lorenzo, braga")
    numbers = inputCleaner("16,4,99")
    date = inputCleaner("")
    schar = inputCleaner("!, @, $, ?")
    iterations = inputCleaner("")
    if (develop == False):
        words = inputCleaner(input("words: "))
        numbers = inputCleaner(input("numbers: "))
        date = inputCleaner(input("date: "))
        schar = inputCleaner(input("special chars: "))
        iterations = input("iteration: ")
    
    startTime = time.time()

    # first stage
    # generating base wordlist

    # processing words
    p_words = set()
    pusher(p_words, words)
    #pusher(p_words, wordsSplitter(p_words))
    pusher(p_words, reverse(p_words))
    pusher(p_words, removeVocals(p_words))
    pusher(p_words, removeConsonants(p_words))
    toBaseWL(p_words)

    #processing numbers
    p_numbers = set()
    pusher(p_numbers, numbers)
    pusher(p_numbers, reverse(numbers))
    toBaseWL(p_numbers)

    #processing special chars
    toBaseWL(schar)
    
    p_simplecomposer = set()
    pusher(p_simplecomposer, simpleComposer(p_words, p_words))
    pusher(p_simplecomposer, simpleComposer(p_words, p_numbers))
    pusher(p_simplecomposer, simpleComposer(p_words, schar))
    string = ""
    for element in schar:
        string = string + element
    print(string)
    elements = wordsSplitter(string)
    print(elements)
    tmp = set()
    for element in elements:
        pusher(tmp, simpleComposer(p_simplecomposer, element))
        pusher(tmp, simpleComposer(element, p_simplecomposer))
        
    pusher(p_simplecomposer, tmp)
    pusher(p_simplecomposer, simpleComposer(p_numbers, schar))
    toBaseWL(p_simplecomposer)



    obfuscated_base_set = set()
    for element in base_wordlist:
        pusher(obfuscated_base_set, obfuscatedChar(element))
    toBaseWL(obfuscated_base_set)

    # second stage
    # generating complex passwords
    toPsw(base_wordlist)
    toPsw(toUpper(base_wordlist))
    obfuscated_base_set = set()
    for element in base_wordlist:
        pusher(obfuscated_base_set, obfuscatedChar(element))
    toBaseWL(obfuscated_base_set)

    # third stage 
    # saving result to wordlist.txt
    passwordsCleaner()
    endTime = time.time()
    print("Generated " + str(len(passwords)) + " passwords in " + str(round(endTime - startTime, 2)))
    save(passwords)

main()