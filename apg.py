# APG v 1.0
# Advanced password generator
#
# by xSyNcr0

print("APG v1.0 by xSyNcr0")
words = input("words: ")
numbers = input("numbers: ")
date = input("date: ")
schar = input("special chars: ")
iterations = input("iteration: ")


base_wordlist = []
passwords = []


def toBaseWL(data):
    if type(data) is list:
        for element in data:
            base_wordlist.append(element)
    else:
        base_wordlist.append(data)

def toPsw(data):
    if type(data) is list:
        for element in data:
            passwords.append(element)
    else:
        passwords.append(data)

def reverse(text):
    if isinstance(text, int):
        text = str(text)
    return text[::-1]

def decodeDate(input):
    base = []
    for element in input:
        base.append(strRemover(input, '-'))
    return base

def strRemover(text, char):
    return text.replace(char, "")

def toUpper(input):
    base = []
    for element in input:
        tmp = []
        tmp.append(element)

        for i in range(len(element)):
            number = i + 1
            for char in 


def CharToSpecialChar(input):
    base = []
    for element in input:
        base.append(element)

def main():
    toBaseWL(numbers)
    for iteration in iterations:
        print(iteration)


main()