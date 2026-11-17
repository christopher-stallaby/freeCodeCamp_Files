""" 
Build a Hash Table
In this lab, you will build a hash table from scratch. 
A hash table is a data structure that stores key-value pairs. A hash table works by taking the key as an input and then hashing this key according to a specific hashing function.

For the purpose of this lab, the hashing function will be simple: it will sum the Unicode values of each character in the key. 
The hash value will then be used as the actual key to store the associated value. The same hash value would also be used to retrieve and delete the value associated with the key.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:
You should define a class named HashTable with a collection attribute initialized to an empty dictionary when a new instance of HashTable is created. 
The collection dictionary should store key-value pairs based on the hashed value of the key.

The HashTable class should have four instance methods: hash, add, remove, and lookup.

The hash method should:
Take a string as a parameter.
Return a hashed value computed as the sum of the Unicode (ASCII) values of each character in the string. You can use the ord function for this computation.

The add method should:
Take two arguments representing a key-value pair, and compute the hash of the key.
Use the computed hash value as a key to store a dictionary containing the key-value pair inside the collection dictionary.
If multiple keys produce the same hash value, their key-value pairs should be stored in the existing nested dictionary under the same hash value. ### REVISIT

The remove method should:
Take a key as its argument and compute its hash.
Confirm if the key exists in the collection.
Remove the corresponding key-value pair from the hash table.
If the key does not exist in the collection, it should not raise an error or remove anything.

The lookup method should:
Take a key as its argument.
Compute the hash of the key, and return the corresponding value stored inside the hash table.
If the key does not exist in the collection, it should return None.

Tests:
Waiting:20. When the 'fcc' key exists in the collection, HashTable().lookup('cfc') should return None.
"""

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        hash = sum(ord(character) for character in string)
        return hash

    def add(self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value

        self.collection.append([hash_value, value])

    def remove(self, key):
        hash_value = self.hash(key)
        bucket = self.collection.get(hash_value)

        if bucket is not None:
            bucket.pop(key, None)
            if not bucket:
                del self.collection[hash_value]

    def lookup(self, key):
        hash_value = self.hash(key)
        if hash_value in self.collection:
            return self.collection[hash_value][key]
        else: 
            return None