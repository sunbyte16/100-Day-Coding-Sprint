class MyHashMap:
    def __init__(self):
        self.size = 10007  # A prime number for the hash table
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h][i] = (key, value)
                return
        self.table[h].append((key, value))
    
    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return -1
    
    def remove(self, key):
        h = self._hash(key)
        for i, (k, v) in enumerate(self.table[h]):
            if k == key:
                self.table[h].pop(i)
                return

def process_queries(queries):
    hashmap = MyHashMap()
    results = []
    
    for query in queries:
        if query[0] == 1:
            _, key, value = query
            hashmap.put(key, value)
        elif query[0] == 2:
            _, key = query
            results.append(hashmap.get(key))
        elif query[0] == 3:
            _, key = query
            hashmap.remove(key)
    
    return results

import sys
input = sys.stdin.read
data = input().strip().split()

# Read number of queries
n = int(data[0])
index = 1

queries = []

for _ in range(n):
    query_type = int(data[index])
    if query_type == 1:
        key = int(data[index + 1])
        value = int(data[index + 2])
        queries.append((1, key, value))
        index += 3
    elif query_type == 2:
        key = int(data[index + 1])
        queries.append((2, key))
        index += 2
    elif query_type == 3:
        key = int(data[index + 1])
        queries.append((3, key))
        index += 2

# Execute queries
results = process_queries(queries)

# Print output for type 2 queries
for result in results:
    print(result)
