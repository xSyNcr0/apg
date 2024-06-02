# Input Output functions

class Input:
    # splitta la stringa "," in set
    @staticmethod
    def cleaner(input_string):
        base = set()
        elements = input_string.split(",")
        for element in elements:
            base.add(element.lower().strip())
        return base

    # decodifica le date
    @staticmethod
    def decodeDate(input_string):
        tmp = input_string.split("-")
        if len(tmp) != 3:
            return None

        return {"year": tmp[0], "month": tmp[1], "day": tmp[2]}
    
    @staticmethod
    def getInt(input_string, default = 4):
        if input_string.isdigit():
            return int(input_string) + 1        
        return default

class Output:        
    # pulisce le password    
    @staticmethod
    def passwordsCleaner(passwords, password_options):
        base = set()
        special_chars = {'!', '@', '#', ',', '.', '<', '>', '/', '?', '~'}
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
        return sorted(base, key=lambda x: (len(x), x.lower()))
    
    # salva le password su wordlist.txt, viene sovreascritto ogni volta
    @staticmethod
    def save(content):
        file = open("wordlist.txt", "w")
        for row in content:
            file.write(row + '\n')
        file.close()
        
        
