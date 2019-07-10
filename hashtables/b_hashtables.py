from doubly_linked_list import DoublyLinkedList

# '''
# Basic hash table key/value pair
# '''


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    idx = 0
    for i, c in enumerate(string):
        idx = (idx + ord(c) * i) % max
    return idx


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    address = hash(key, hash_table.capacity)
    if hash_table.storage[address] is None:
        hash_table.storage[address] = DoublyLinkedList()
    hash_table.storage[address].add_to_head(Pair(key, value))

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    address = hash(key, hash_table.capacity)
    current_bucket = hash_table.storage[address]
    if current_bucket is None:
        print("You can't remove a value that doesn't exist, friend.")
    else:
        current_bucket.find_and_delete_key(key)

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    address = hash(key, hash_table.capacity)
    current_bucket = hash_table.storage[address]
    if current_bucket is None:
        return None
    current_node = current_bucket.head
    while current_node:
        if current_node.value.key == key:
            return current_node.value.value
        current_node = current_node.next
    return None


def hash_table_resize(hash_table):
    new_hash = HashTable(hash_table.capacity * 2)

    # Copy over elements
    for dll in hash_table.storage:
        if dll is not None:
            current_node = dll.head
            while current_node:
                hash_table_insert(new_hash,
                                  current_node.value.key,
                                  current_node.value.value)
                current_node = current_node.next

    return new_hash


def Testing():
    ht = HashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")

    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
