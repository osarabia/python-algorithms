import unittest
#hash table implementation linked link collision
CAPACITY = 60

class HashTable:
    def __init__(self):
        self.capacity = CAPACITY
        self.size = 0
        self.container = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for i, c in enumerate(key):
            hashsum += (i + len(key) ** ord(c))
            hashsum = hashsum % self.capacity

        return hashsum

    def put(self, key, value):
        self.size += 1

        arrayIndex = self.hash(key)
        node = self.container[arrayIndex]
        if node is None:
            self.container[arrayIndex]= Node(key, value)
            return

        prev = node
        while prev.next is not None:
            prev = prev.next
        prev.next = Node(key, value)

    def get(self, key):
        arrayIndex = self.hash(key)
        node = self.container[arrayIndex]
        while node is not None and node.key != key:
            node = node.next

        if node:
            return node.value

        return None


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class TestHashTable(unittest.TestCase):
    def test_hash_function(self):
        #arrange
        #test diff lengths strings
        cases = [
            "door",
            "kitchen",
            "oven",
            "chair",
            "refrigerator"
        ]
        output = []
        myHashTable = HashTable()
        maxIndexValue = len(myHashTable.container)

        for c in cases:
            #action
            hashValue = myHashTable.hash(c)
            output.append(hashValue)

        #assert
        assert output[0] <= maxIndexValue, "expecting value less than {}, got {}".format(maxIndexValue, output[0])
        assert output[1] <= maxIndexValue, "expecting value less than {}, got {}".format(maxIndexValue, output[1])
        assert output[2] <= maxIndexValue, "expecting value less than {}, got {}".format(maxIndexValue, output[2])
        assert output[3] <= maxIndexValue, "expecting value less than {}, got {}".format(maxIndexValue, output[3])
        assert output[4] <= maxIndexValue, "expecting value less than {}, got {}".format(maxIndexValue, output[4])


    def test_put_from_empty_table(self):
        #arrange
        cases = [
            ("door", "brown"),
            ("kitchen", "black"),
            ("oven", "white"),
            ("chair", "pink"),
            ("refrigerator", "blue")
        ]
       
        for c in cases:
            k,v = c
            #action
            myHashTable = HashTable()
            myHashTable.put(k,v)

            #assert
            index = myHashTable.hash(k)
            got =  myHashTable.container[index]
            assert v == got.value, "expecting {}, got {}".format(v, got.value)
            assert k == got.key, "expecting {}, got {}".format(k, got.key)

    def test_get(self):
        #arrange
        cases = [
            ("door", "brown"),
            ("kitchen", "black"),
            ("oven", "white"),
            ("chair", "pink"),
            ("refrigerator", "blue")
        ]
        myHashTable = HashTable()

       
        for c in cases:
            k,v = c
            #action
            myHashTable.put(k,v)
            valueFromTable = myHashTable.get(k)

            #assert
            assert v == valueFromTable, "expecting {}, got {}".format(v, valueFromTable)

    def test_get_missing_key(self):
        #arrange
        key, value = "name", "charles"
        myHashTable = HashTable()
        myHashTable.put(key,value)

        #action
        value = myHashTable.get("lastname")

        #assert
        assert value == None, "expecting {}, got {}".format(None, value)


if __name__ == "__main__":
    unittest.main()
