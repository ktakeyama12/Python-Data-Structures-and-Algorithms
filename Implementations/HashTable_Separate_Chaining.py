# Hash Map (Hash Table)
# Reference https://github.com/joeyajames/Python/blob/master/HashMap.py

class HashMap:
    def __init__(self):
        self.size = 6  # Size is usually larger
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)  # Uses ASCII value for each letter in key
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:  # No collision
            self.map[key_hash] = list([key_value])
            return True
        else:  # Collision
            for pair in self.map[key_hash]:
                if pair[0] == key:  # If key exists, we update value
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)  # If it doesn't, just add
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:  # Key value pair does not exist
            return False
        for i in range (0, len(self.map[key_hash])):  # We need the index to remove
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)  # Use pop to remove index
                return True
        return False

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))