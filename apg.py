# APG v 1.0
# Advanced password generator
#
# by xSyNcr0
import time
from in_out import Input, Output
from set import SetManipolator
from firstStage import FirstStage

develop = True
base_wordlist = set()
passwords = set()
min_char = 8
max_char = 28
pad = 4 
iterations = 4
password_options = {"min_char": min_char, "max_char": max_char, "contains_uppercase": False, "contains_lowercase": True, "contains_special_chars": False, "contains_numbers": True, "padNumber": pad}

def main():
    print("APG v1.0 by xSyNcr0")

    # input stage
    words = Input.cleaner("Gabriele, Braga, Lorenzo")
    numbers = Input.cleaner("")
    dates = Input.cleaner("2012-04-28, 1999-04-16")
    schars = Input.cleaner("!, @, $, ?, _, -, .") #"!, @, $, ?, _, -"
    pad = Input.getInt("2")
    
    if (develop == False):
        words = Input.cleaner(input("words: "))
        numbers = Input.cleaner(input("numbers: "))
        dates = Input.cleaner(input("dates: "))
        schars = Input.cleaner(input("special chars: "))
        pad = Input.getInt(input("pads: "), 4)
    
    startTime = time.time()

    # Parole
    for word in words:
        SetManipolator.toFetching(word)       
        SetManipolator.toFetching(FirstStage.reverse(word))  
           
        combinazioni = FirstStage.wordsSplitter(word)
        for combinazione in combinazioni:
            SetManipolator.toFetching(combinazione)     
            SetManipolator.toFetching(FirstStage.removeConsonants(combinazione))
            SetManipolator.toFetching(FirstStage.removeVocals(combinazione))
            
        combinazioni = FirstStage.wordsSplitter(FirstStage.reverse(word))
        for combinazione in combinazioni:
            SetManipolator.toFetching(combinazione)     
            SetManipolator.toFetching(FirstStage.removeConsonants(combinazione))
            SetManipolator.toFetching(FirstStage.removeVocals(combinazione))
            
    # Numeri
    for number in numbers:
        SetManipolator.toFetching(number)
        SetManipolator.toFetching(FirstStage.wordsSplitter(number))
        
    # date
    for date in dates:
        SetManipolator.toFetching(date)
        tmp = Input.decodeDate(date)
        if tmp is None:
            continue
        
        SetManipolator.toFetching(tmp["year"] + "-" + tmp["month"] + "-" + tmp["day"])
        SetManipolator.toFetching(tmp["year"] + "/" + tmp["month"] + "/" + tmp["day"])
        
        SetManipolator.toFetching(tmp["day"] + "-" + tmp["month"] + "-" + tmp["year"])
        SetManipolator.toFetching(tmp["day"] + "/" + tmp["month"] + "/" + tmp["year"])    
        
        SetManipolator.toFetching(tmp["day"] + tmp["month"] + tmp["year"])
        SetManipolator.toFetching(tmp["year"] + tmp["month"] + tmp["day"])
        SetManipolator.toFetching(tmp["year"] + tmp["day"])
        SetManipolator.toFetching(tmp["year"] + tmp["month"])
        SetManipolator.toFetching(tmp["month"] + tmp["day"])
        SetManipolator.toFetching(tmp["day"] + tmp["month"])
        SetManipolator.toFetching(tmp["day"] + tmp["year"])
        
        SetManipolator.toFetching(FirstStage.wordsSplitter(tmp["day"]))
        SetManipolator.toFetching(FirstStage.wordsSplitter(tmp["month"]))
        SetManipolator.toFetching(FirstStage.wordsSplitter(tmp["year"]))
        
        SetManipolator.toFetching(FirstStage.wordsSplitter(FirstStage.reverse(str(tmp["day"]))))
        SetManipolator.toFetching(FirstStage.wordsSplitter(FirstStage.reverse(str(tmp["month"]))))
        SetManipolator.toFetching(FirstStage.wordsSplitter(FirstStage.reverse(str(tmp["year"]))))
        
    # caratteri speciali
    for schar in schars:
        SetManipolator.toFetching(schar)
        
    # Aggiunta pad ai numeri
    for i in range(pad):
        padded_element = set()
        for fetching in SetManipolator.fetching:
            padded = FirstStage.padNumber(fetching, i)
            if padded is None:
                continue
            SetManipolator.pusher(padded_element, padded)
        SetManipolator.toFetching(padded_element)
        
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
            
    
    for string in SetManipolator.base_wordlist:
        for number in SetManipolator.numbers:
            for schar in SetManipolator.schars:
                SetManipolator.toPasswords(string + number)
                SetManipolator.toPasswords(string.capitalize() + number)
                SetManipolator.toPasswords(string + number + schar)
                SetManipolator.toPasswords(string.capitalize() + number + schar)
    
    # Output stage
    SetManipolator.passwords = Output.passwordsCleaner(SetManipolator.passwords, password_options)
    endTime = time.time()
    print("Generated " + str(len(SetManipolator.passwords)) + " passwords in " + str(round(endTime - startTime, 2)))
    Output.save(SetManipolator.passwords)

main()
