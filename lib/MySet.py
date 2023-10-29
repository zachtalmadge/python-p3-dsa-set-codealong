class MySet:

    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True # Add a value as a key on the Dictionary
        return self                   # Return the updated set
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)


