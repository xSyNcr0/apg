# APG v 1.0
# Advanced password generator
#
# by xSyNcr0

print("APG v1.0 by xSyNcr0")
words = input("words: ").split(",")
numbers = input("numbers: ").split(",")
date = input("date: ").split(",")
schar = input("special chars: ").split(",")
iterations = input("iteration: ")


base_wordlist = set()
passwords = set()


def toBaseWL(data):
    if isinstance(data, set):
        for element in data:
            base_wordlist.add(element)
    elif isinstance(data, list):
        for element in data:
            passwords.add(element)
    else:
        base_wordlist.add(data)

def toPsw(data):
    if isinstance(data, set):
        for element in data:
            passwords.add(element)
    elif isinstance(data, list):
        for element in data:
            passwords.add(element)
    else:
        passwords.add(data)

def reverse(text):
    if isinstance(text, int):
        text = str(text)
    return text[::-1]

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


def CharToSpecialChar(input):
    base = set()
    for element in input:
        base.add(element)

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

def save():
    content = sorted(base_wordlist)
    file = open("wordlist.txt", "w")
    for row in content:
        file.write(row + '\n')
    file.close()

def main():
    toBaseWL(words)
    toBaseWL(toUpper(words))
    print(len(base_wordlist))
    print(base_wordlist)
    passwords = base_wordlist
    save()
    


main()