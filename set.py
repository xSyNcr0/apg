# Array functions
class SetManipolator:
    input_strings = set()
    base_wordlist = set()
    passwords = set()    
    fetching = set()
    numbers = set()
    schars = set()
    iterated_wordlist = set()
        
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
    def toFetching(data):
        SetManipolator.pusher(SetManipolator.fetching, data)

    @staticmethod
    def toBaseWL(data):
        SetManipolator.pusher(SetManipolator.base_wordlist, data)

    @staticmethod
    def toPasswords(data):
        SetManipolator.pusher(SetManipolator.passwords, data)
