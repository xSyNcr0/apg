# APG v 1.0
# Advanced password generator
#
# by xSyNcr0
import time
from in_out import Input, Output
from set import SetManipolator
from firstStage import FirstStage
from secondStage import SecondStage
import datetime
import sys
from colorama import init, Fore, Back, Style
import os

def clear_terminal():
    # Controlla il sistema operativo
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix / Linux / macOS
        os.system('clear')

# Utilizz
clear_terminal()


develop = False

init()
def main():
    print(Fore.GREEN + Style.BRIGHT + """
                     _____   _____ 
               /\   |  __ \ / ____|
              /  \  | |__) | |  __ 
             / /\ \ |  ___/| | |_ |
            / ____ \| |    | |__| |
           /_/    \_\_|     \_____| v1.0
                         
    """)
    print(Fore.WHITE + "         :: Advanced Password Generator ::\n        " + Fore.BLUE + "           by xSyNcr0\n")
    print("  " + Style.RESET_ALL + Fore.WHITE + Back.RED + "::" +  Style.RESET_ALL + " Disclaimer: Developer assume no liability " + Fore.WHITE + Back.RED + "::" + Style.RESET_ALL)
    print("  " + Fore.WHITE + Back.RED + "::" +  Style.RESET_ALL + " and is not responsible for any issue or   " + Fore.WHITE + Back.RED + "::" + Style.RESET_ALL)
    print("  " + Fore.WHITE + Back.RED + "::" +  Style.RESET_ALL + "           damage caused by APG            " + Fore.WHITE + Back.RED + "::" + Style.RESET_ALL)
    print("\n\n\n")
    
    min_char = 8
    max_char = 14
    min_digit = 1
    max_digit = 2
    min_schars = 0
    max_schars = 2
    min_uppercase = 0
    max_uppercase = 2
    pad = 0 
    year_min = ""
    year_max = ""
    psw_level = 2
    obfuscation_level = 1
    obfuscation_iterations = 1
    enable_plus_one = 0

    password_options = {
        "min_char": min_char, "max_char": max_char, 
        "min_special_chars": 1, "max_special_chars": 1,
        "min_digit": 1, "max_digit": 2,
        "min_uppercase": 0, "max_uppercase": 1,
        "pad_number": pad
        }

    # input stage
    words = Input.cleaner("")
    numbers = Input.cleaner("")
    dates = Input.cleaner("")
    schars = Input.cleaner("") #!, @, $, ?, _, -, .
    year_min, year_max = Input.get_min_max("")
    pad = Input.get_int("2")
    # aggiungere obfuscation
    psw_level = Input.get_int("2")
    obfuscation_iterations = 1
    
    if (develop == False):        
        words = Input.cleaner(input(Fore.YELLOW + Style.BRIGHT + "Words\n" + Fore.CYAN + "Format: " + Fore.GREEN + Style.NORMAL + "word1, word2, word3, ...\n" + Fore.WHITE))
        numbers = Input.cleaner(input(Fore.YELLOW + Style.BRIGHT + "\nNumbers\n" + Fore.CYAN + "Format: " + Fore.GREEN + Style.NORMAL + "num1, num2, num3, ...\n" + Fore.WHITE))
        dates = Input.cleaner(input(Fore.YELLOW + Style.BRIGHT + "\nDates\n" + Fore.CYAN + "Format: " + Fore.GREEN + Style.NORMAL + "yyyy-mm-dd, yyyy-mm-dd, ...\n" + Fore.WHITE))
        schars = Input.cleaner(input(Fore.YELLOW + Style.BRIGHT + "\nSpecial chars\n" + Fore.CYAN + "Example: " + Fore.GREEN + Style.NORMAL + "@, &, !" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "char, char, char\n" + Fore.WHITE))
        psw_level = Input.get_int(input(Fore.YELLOW + Style.BRIGHT + "\nPasswords crack level\n" + Fore.CYAN + "Example: " + Fore.GREEN + Style.NORMAL + "2" + Fore.CYAN + Style.BRIGHT + "\nFormat [1 to 5]: " + Fore.GREEN + Style.NORMAL + "digit\n" + Fore.WHITE))
        enable_plus_one = Input.get_int(input(Fore.YELLOW + Style.BRIGHT + "\nPlus one\n" + Fore.CYAN + "Example: " + Fore.GREEN + Style.NORMAL + "1 -> [3, 99] = [3, 4, 99, 100]" + Fore.CYAN + Style.BRIGHT + "\nFormat [0 (no effect), 1]: " + Fore.GREEN + Style.NORMAL + "digit\n" + Fore.WHITE))
        
        min_char, max_char = Input.get_min_max(input(Fore.YELLOW + Style.BRIGHT + "\nPasswords length" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "8, 14 -> psw length 8, 9, 10, 11, 12, 13, 14" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "min_length, max_length\n" + Fore.WHITE))
        min_digit, max_digit = Input.get_min_max(input(Fore.YELLOW + Style.BRIGHT + "\nNumbers digit" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "0, 2 -> psw with 0, 1, 2 numbers digit" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "min_length, max_length\n" + Fore.WHITE))
        min_schars, max_schars = Input.get_min_max(input(Fore.YELLOW + Style.BRIGHT + "\nSpecial chars" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "0, 2 -> psw with 0, 1, 2 special chars" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "min_length, max_length\n" + Fore.WHITE))
        min_uppercase, max_uppercase = Input.get_min_max(input(Fore.YELLOW + Style.BRIGHT + "\nUppercase chars" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "0, 2 -> psw with 0, 1, 2 uppercase chars" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "min_length, max_length\n" + Fore.WHITE))
        year_min, year_max = Input.get_min_max(input(Fore.YELLOW + Style.BRIGHT + "\nYears loop" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "2016, 2021 -> [2016, 2017, 2018, 2019, 2020, 2021]" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "year_min, year:max\n" + Fore.WHITE))

        if psw_level >= 2:
            pad = Input.get_int(input(Fore.YELLOW + Style.BRIGHT + "\nPadded numbers" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "2 -> [3] = [3, 03]" + Fore.CYAN + Style.BRIGHT + "\nFormat: " + Fore.GREEN + Style.NORMAL + "digit\n" + Fore.WHITE))
            obfuscation_level = Input.get_int(input(Fore.YELLOW + Style.BRIGHT + "\nObfuscation level" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "1 -> [hello] = [h3llo, hell0]" + Fore.CYAN + Style.BRIGHT + "\nFormat [0 (no effect) to 3]: " + Fore.GREEN + Style.NORMAL + "digit\n" + Fore.WHITE))
            if obfuscation_level >= 1:
                obfuscation_iterations = Input.get_int(input(Fore.YELLOW + Style.BRIGHT + "\nObfuscation iterations" + Fore.CYAN + "\nExample: " + Fore.GREEN + Style.NORMAL + "1 -> [hello] = [h3llo, hell0, h3ll0]" + Fore.CYAN + Style.BRIGHT + "\nFormat [1 to 99]: " + Fore.GREEN + Style.NORMAL + "digit\n" + Fore.WHITE))
        print("\n\n")
        
    
    password_options = {
        "min_char": min_char, "max_char": max_char, 
        "min_special_chars": min_schars, "max_special_chars": max_schars,
        "min_digit": min_digit, "max_digit": max_digit,
        "min_uppercase": min_uppercase, "max_uppercase": max_uppercase,
        "pad_number": pad
        }
                
    start_time = time.time()
    Output.password_options = password_options
    Output.init_file_passwords()
    
    # Parole
    for word in words:
        SetManipolator.to_fetching(word)                 
        SetManipolator.to_fetching(FirstStage.remove_consonants(word))
        SetManipolator.to_fetching(FirstStage.remove_vocals(word))         
        combinazioni = FirstStage.word_cutter(word)
        for combinazione in combinazioni:
            SetManipolator.to_fetching(combinazione)     
            SetManipolator.to_fetching(FirstStage.remove_consonants(combinazione))
            SetManipolator.to_fetching(FirstStage.remove_vocals(combinazione))
            
        SetManipolator.to_fetching(FirstStage.reverse(word))  
        SetManipolator.to_fetching(FirstStage.remove_consonants(FirstStage.reverse(word)))
        SetManipolator.to_fetching(FirstStage.remove_vocals(FirstStage.reverse(word)))
        combinazioni = FirstStage.word_cutter(FirstStage.reverse(word))
        for combinazione in combinazioni:
            SetManipolator.to_fetching(combinazione)     
            SetManipolator.to_fetching(FirstStage.remove_consonants(combinazione))
            SetManipolator.to_fetching(FirstStage.remove_vocals(combinazione))
            
            
    # Numeri
    for number in numbers:
        SetManipolator.to_fetching(number)
        SetManipolator.to_fetching(FirstStage.word_splitter(number))
        
    # date
    for date in dates:
        SetManipolator.to_fetching(date)
        tmp = Input.decode_date(date)
        if tmp is None:
            continue
        
        #SetManipolator.to_fetching(tmp["year"] + "-" + tmp["month"] + "-" + tmp["day"])
        #SetManipolator.to_fetching(tmp["year"] + "/" + tmp["month"] + "/" + tmp["day"])
        
        #SetManipolator.to_fetching(tmp["day"] + "-" + tmp["month"] + "-" + tmp["year"])
        #SetManipolator.to_fetching(tmp["day"] + "/" + tmp["month"] + "/" + tmp["year"])    
        if psw_level >= 4:
            SetManipolator.to_fetching(tmp["day"] + tmp["month"] + tmp["year"])
            SetManipolator.to_fetching(tmp["year"] + tmp["month"] + tmp["day"])
        SetManipolator.to_fetching(tmp["year"] + tmp["day"])
        SetManipolator.to_fetching(tmp["year"] + tmp["month"])
        SetManipolator.to_fetching(tmp["month"] + tmp["day"])
        SetManipolator.to_fetching(tmp["day"] + tmp["month"])
        SetManipolator.to_fetching(tmp["day"] + tmp["year"])
        
        SetManipolator.to_fetching(FirstStage.word_splitter(tmp["day"]))
        SetManipolator.to_fetching(FirstStage.word_splitter(tmp["month"]))
        SetManipolator.to_fetching(FirstStage.word_splitter(tmp["year"]))
        
        SetManipolator.to_fetching(FirstStage.word_splitter(FirstStage.reverse(str(tmp["day"]))))
        SetManipolator.to_fetching(FirstStage.word_splitter(FirstStage.reverse(str(tmp["month"]))))
        SetManipolator.to_fetching(FirstStage.word_splitter(FirstStage.reverse(str(tmp["year"]))))
        
    # caratteri speciali
    for schar in schars:
        SetManipolator.to_fetching(schar)
        
    # anni
    if year_min != "" and year_max != "":
        for year in range(year_min, year_max, 1):
            combinazioni = set({str(year), FirstStage.reverse(str(year))})
            for combinazione in combinazioni:            
                SetManipolator.to_fetching(combinazione)
                SetManipolator.to_fetching(combinazione[:2])
                SetManipolator.to_fetching(combinazione[-2:])    
    
      
    # piu uno
    if enable_plus_one == 1:
        plus_one = set()
        for element in SetManipolator.fetching:
            if element.isdigit():
                SetManipolator.pusher(plus_one, str(int(element) + 1))
        SetManipolator.to_fetching(plus_one)
      
    # Aggiunta pad ai numeri
    for i in range(pad):
        padded_element = set()
        for fetching in SetManipolator.fetching:
            padded = FirstStage.pad_number(fetching, i)
            if padded is None:
                continue
            SetManipolator.pusher(padded_element, padded)
        SetManipolator.to_fetching(padded_element)
        
    #
    # FINE FETCHING
    # INIZIO FIRST STAGE
    # wordlist base creata
    #
    
    SetManipolator.base_wordlist = SetManipolator.fetching  
    SetManipolator.schars = schars
    # lo riempio con i numeri della wordlist
    for number in SetManipolator.base_wordlist:
        if number.isdigit():
            SetManipolator.pusher(SetManipolator.numbers, number)
    
    base_wordlist = list(SetManipolator.base_wordlist)
    schars = list(SetManipolator.schars)
    numbers = list(SetManipolator.numbers)
    for string1 in base_wordlist:
        combinations = [string1, string1.capitalize()]
        
        for combinazione in combinations:
            SetManipolator.to_passwords(combinazione)

        for string2 in base_wordlist:
            combinations = [
                (string1, string2),
                (string1.capitalize(), string2),
            ]
            if psw_level >= 2:
                combinations.append((string1, string2.capitalize()))
                combinations.append((string1.capitalize(), string2.capitalize()))
                
            for str1, str2 in combinations:
                SetManipolator.to_passwords(str1 + str2)

                for schar1 in schars:
                    SetManipolator.to_passwords(str1 + schar1 + str2)
                
                for number in numbers:
                    SetManipolator.to_passwords(str1 + number)
                    SetManipolator.to_passwords(str1 + str2 + number)
                    
                    for schar1 in schars:
                        SetManipolator.to_passwords(str1 + number + schar1)
                        if psw_level >= 3:
                            SetManipolator.to_passwords(str1 + schar1 + str2 + number)
                        
                            if psw_level >= 4:
                                for schar2 in schars:
                                    SetManipolator.to_passwords(str1 + schar1 + str2 + number + schar2)
                                
                                if psw_level >= 5:
                                    for schar3 in schars:
                                        SetManipolator.to_passwords(schar1 + str1 + schar2 + str2 + number + schar3)
    
    #
    # SECOND STAGE
    # INIT
    #
    SecondStage.obfuscation_level = obfuscation_level
    SecondStage.obfuscation_iterator = obfuscation_iterations
    if SecondStage.obfuscation_level > 1:
        obfuscated_passwords = set()
        for password in SetManipolator.passwords:
            SetManipolator.pusher(obfuscated_passwords, SecondStage.obfuscator(password))
        SetManipolator.passwords.update(obfuscated_passwords)
        
    # Output stage
    SetManipolator.passwords = Output.passwords_cleaner(SetManipolator.passwords, True)
    end_time = time.time()    
    sys.stdout.write('\r' + "Passwords generated: " + str(len(SetManipolator.passwords)) + " in " + str(round(end_time - start_time, 2)) + "s\nSaving...\n")
    
    # Saving first stage
    time.sleep(0.2)
    Output.save(SetManipolator.passwords)
    SetManipolator.passwords = set()
    print("Saved in wordlist.txt")

main()
