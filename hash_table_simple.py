class HashTable(object):
    """Simple hash basic practice (beware, not practical!)"""
    def __init__(self, size=10000):
        self.table = [None]*size
        self.size = size

    def store(self, string):
        """Input a string that's stored in
        the table."""
        index = self.calculate_hash_value(string) % self.size

        if self.table[index] is None:
            self.table[index] = [string]
        else:
            self.table[index].append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash = self.calculate_hash_value(string)
        index = hash % self.size

        if self.table[index] and string in self.table[index]:
                return hash
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
        return ord(string[0])*100 + ord(string[1])


if __name__ == "__main__":
    hash_table = HashTable()
    print(hash_table.calculate_hash_value('Hello'))

    print(hash_table.lookup('Hello'))

    hash_table.store('Hey')
    print(hash_table.lookup('Hey'))

    hash_table.store('Hello')
    print(hash_table.lookup('Hello'))
