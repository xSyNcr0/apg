
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

