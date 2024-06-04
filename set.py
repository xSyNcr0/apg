# Array functions
import sys
from in_out import Input, Output

class SetManipolator:
    input_strings = set()
    base_wordlist = set()
    passwords = set()    
    fetching = set()
    numbers = set()
    schars = set()
    max_megabytes = 64
    passwords_counter = 0
    spin_index = 0
    spin_password_counter = 0
        
    @staticmethod
    def pusher(array, data):
        if isinstance(data, set):
            for element in data:
                array.add(element)
        elif isinstance(data, list):
            for element in data:
                array.append(element)
        else:
            array.add(data)

    @staticmethod
    def to_fetching(data):
        SetManipolator.pusher(SetManipolator.fetching, data)


    @staticmethod
    def to_passwords(data, saver = False):   
        tmp = data
        if saver == True:   
            tmp = Output.passwordsCleaner(data) 
            
        if len(tmp) == 0:
            return
        
        SetManipolator.passwords_counter = SetManipolator.passwords_counter + 1
        last_pass = ''
        if isinstance(data, str):
            last_pass = data
        #sys.stdout.write('\r' + last_pass + ' ' * 20)
        
        spin_chars = ['|', '/', '-', '\\']
        SetManipolator.spin_password_counter = SetManipolator.spin_password_counter + 1
        if SetManipolator.spin_password_counter >= 35000: # 0.5 sec 
            SetManipolator.spin_index = (SetManipolator.spin_index + 1) % 4
            SetManipolator.spin_password_counter = 0
        
        sys.stdout.write('\r' + "psw: " + last_pass + ' ' * (28 - len(last_pass)) + spin_chars[SetManipolator.spin_index])
        sys.stdout.flush() # important
        
        SetManipolator.pusher(SetManipolator.passwords, tmp)
        if saver == True:
            actul_mb = sys.getsizeof(SetManipolator.passwords) / (1024 ** 2)
            if (actul_mb >= SetManipolator.max_megabytes):
                Output.save(SetManipolator.passwords)
                SetManipolator.passwords = set()
            
            

    