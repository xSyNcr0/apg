# First stage functions

class FirstStage:
    # inverte la stringa
    @staticmethod
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

    # Rimuove vocale
    @staticmethod
    def remove_vocals(input):
        if isinstance(input, set):
            base = set()
            for element in input:
                base.add(remove_vocals(element))
            return base
        elif isinstance(input, str):
            return input.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

    # Rimuove consonanti
    @staticmethod
    def remove_consonants(input_data):
        if isinstance(input_data, set):
            result_set = set()
            for element in input_data:
                result_set.update(remove_consonants(element))
            return result_set
        elif isinstance(input_data, list):
            result_list = []
            for element in input_data:
                result_list.extend(remove_consonants(element))
            return result_list
        elif isinstance(input_data, str):
            return ''.join(char for char in input_data if char.lower() in 'aeiou')
        else:
            return input_data

    @staticmethod
    def word_splitter(input):
        if isinstance(input, (set, list)):
            base = set()
            for element in input:
                pusher(base, word_splitter(element))
            return base
        elif isinstance(input, str):
            result_set = set()
            n = len(input)

            for i in range(1 << n):
                combination = [input[j] for j in range(n) if (i >> j) & 1]
                result_set.add(''.join(combination))
            return result_set
        
    @staticmethod
    def pad_number(input_string, padSize = 2):
        if input_string.isdigit():
            if len(input_string) < padSize:
                return input_string.zfill(padSize)
        return None
    
    @staticmethod
    def word_cutter(input_string):
        base = set()
        for index in range(len(input_string)):
            base.add(input_string[0: index])            
        return base