class SecondStage:
    base_chars = ['a', 'e', 'i', 'o', 's', 'c', 'g', 'l', 't', 'b']
    obfuscated_chars = ['@', '4', '3', '!', '1', '0', '$', '(', '9', '|', '5', '7', '8', '{', '+']
    obfuscation_level = 0
    obfuscation_iterator = 1

    @staticmethod
    def obfuscator(input):
        if isinstance(input, set):
            base = set()
            for element in input:
                base.add(SecondStage.obfuscatedChar(element))
            return base
        elif isinstance(input, str):
            return SecondStage.mapper_obfucator_chars(input)

    @staticmethod
    def mapper_obfucator_chars(string, iteration=1):
        result_set = set()
        if iteration > SecondStage.obfuscation_iterator:
            return result_set

        for i in range(len(string)):
            current_char = string[i].lower()
            
            if SecondStage.obfuscation_level >= 1:                        
                if current_char == 'a':
                    result_set.add(string[:i] + '@' + string[i+1:])
                    result_set.add(string[:i] + '4' + string[i+1:])                        
                elif current_char == 'e':
                    result_set.add(string[:i] + '3' + string[i+1:])
                elif current_char == 'i':
                    result_set.add(string[:i] + '!' + string[i+1:])
                    result_set.add(string[:i] + '1' + string[i+1:])
                elif current_char == 'o':
                    result_set.add(string[:i] + '0' + string[i+1:])
                elif current_char == 's':
                    result_set.add(string[:i] + '$' + string[i+1:])
                    
            if SecondStage.obfuscation_level >= 2:
                if current_char == 'c':
                    result_set.add(string[:i] + '(' + string[i+1:])
                elif current_char == 'g':
                    result_set.add(string[:i] + '9' + string[i+1:])
                elif current_char == 'l':
                    result_set.add(string[:i] + '|' + string[i+1:])
                    result_set.add(string[:i] + '1' + string[i+1:])
                elif current_char == 's':
                    result_set.add(string[:i] + '5' + string[i+1:])
                elif current_char == 't':
                    result_set.add(string[:i] + '7' + string[i+1:])
                    
            if SecondStage.obfuscation_level >= 3:
                if current_char == 'b':
                    result_set.add(string[:i] + '8' + string[i+1:])
                elif current_char == 'c':
                    result_set.add(string[:i] + '{' + string[i+1:])
                elif current_char == 't':
                    result_set.add(string[:i] + '+' + string[i+1:])
        
        if iteration < SecondStage.obfuscation_iterator:
            next_result_set = set(result_set)  # Copia i risultati della prima iterazione
            for result in result_set:
                next_result_set.update(SecondStage.mapper_obfucator_chars(result, iteration + 1))
            result_set = next_result_set

        return result_set
