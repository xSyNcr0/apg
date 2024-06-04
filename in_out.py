# Input Output functions
class Input:
    @staticmethod
    def cleaner(input_string):
        base = set()
        elements = input_string.split(",")
        for element in elements:
            base.add(element.lower().strip())
        return base

    # decodifica le date
    @staticmethod
    def decode_date(input_string):
        tmp = input_string.split("-")
        if len(tmp) != 3:
            return None

        return {"year": tmp[0], "month": tmp[1], "day": tmp[2]}
    
    @staticmethod
    def get_int(input_string, default = 4):
        if input_string.isdigit():
            return int(input_string)        
        return default
    
    @staticmethod
    def get_min_max(str, min = "", max = ""):
        elements = str.split(',')
        new_elements = []
        for element in elements:
            if element.strip().isdigit():
                new_elements.append(int(element.strip()))
                
        elements = new_elements
        if len(elements) == 0:
            return min, max
        
        min = elements[0]
        max = elements[0]
        for element in elements:
            if element < min:
                min = element
            
            if element > max:
                max = element
                
        return min, max

class Output:        
    # pulisce le password    
    password_options = None
    @staticmethod
    def passwords_cleaner(passwords, sort = False):
        password_options = Output.password_options
        base = set()
        special_chars = {'!', '@', '#', ',', '.', '<', '>', '/', '?', '~', '-', '_'}
        if isinstance(passwords, str):
            passwords = set({passwords})
            
        for password in passwords:
            if (len(password) < password_options["min_char"]) or (len(password) > password_options["max_char"]):
                continue
            
            # Controllo caratteri speciali
            special_char_count = sum(1 for char in password if char in special_chars)
            if (special_char_count < password_options["min_special_chars"] or
                special_char_count > password_options["max_special_chars"]):
                continue
            
            # Controllo numeri
            digit_count = sum(1 for char in password if char.isdigit())
            if (digit_count < password_options["min_digit"] or
                digit_count > password_options["max_digit"]):
                continue        
            
            # Controllo caratteri maiuscoli
            uppercase_count = sum(1 for char in password if char.isupper())
            if (uppercase_count < password_options["min_uppercase"] or
                uppercase_count > password_options["max_uppercase"]):
                continue

            base.add(password)
        if sort == False:
            return base
        return sorted(base, key=lambda x: (len(x), x.lower()))
    
    # salva le password su wordlist.txt, viene sovreascritto ogni volta
    @staticmethod
    def save(content):
        file = open("wordlist.txt", "a")
        for row in content:
            file.write(row + '\n')
        file.close()
        
        
    @staticmethod
    def init_file_passwords():
        file = open("wordlist.txt", "w")
        file.write("")
        file.close()
        
    @staticmethod
    def wordlist_cleaner():
        file = open("wordlist.txt", "r")
        lines = file.readlines()
        
        passwords = Output.passwords_cleaner(lines, True)
        
        file = open("wordlist.txt", "w", encoding='utf-8')
        for password in passwords:
            file.write(password)
            
    @staticmethod
    def passwords_counter():        
        file = open("wordlist.txt", "r")
        lines = file.readlines()
        return len(lines)
    
    @staticmethod
    def load_from_wordlist():
        file = open("wordlist.txt", "r")
        lines = file.readlines()
        return len(lines)
        
        
        
        
        
