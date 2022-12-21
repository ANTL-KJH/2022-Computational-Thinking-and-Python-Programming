# myHashMap
class Entry():
    def __init__(self, k, v):               # init Entry
        self._key = k
        self._value = v

    def __str__(self):                      # printout str
        return str(self._value)

class Bucket(Entry):
    def __init__(self):                     # init Bucket
        self._bucket = []

    def _getitem(self, k):                  # get item at the bucket
        for item in self._bucket:
            if k == item._key:
                return item._value
        return None

    def _setitem(self, k, v):               # set item
        for item in self._bucket:
            if k == item._key:              # if key is duplicated, change value and return
                item._value = v
                return
        self._bucket.append(Entry(k, v))    # append Entry at the Bucket

    def _delitem(self, k):
        for j in range(len(self._bucket)):
            if k == self._bucket[j]._key:   # find key
                self._bucket.pop(j)
                return 1                    # if deleting item is successful, return 1
        return None

    def __len__(self):
        return len(self._bucket)

    def __iter__(self):                     # provides iterator as generator function
        for item in self._bucket:
            yield item._key

class HashMap(Bucket):
    def __init__(self, capacity=11, prm=109345121): # init HashMap
        self._hash_tbl = capacity * [None]
        self._hash_tbl_size = capacity
        self._num_entry = 0
        self._prime = prm

    def _hash_value(self, k):                       # hash value
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size

    def __len__(self):
        return self._num_entry

    def _getitem(self, k):                          # get item
        hv = self._hash_value(k)                    # hash value
        # print("key({}) => hash_tbl[{}]".format(k, hv))
        bucket = self._hash_tbl[hv]                 # get bucket
        return bucket._getitem(k)

    def _setitem(self, k, v):                       # set item
        hv = self._hash_value(k)                    # hash value
        if self._hash_tbl[hv] is None:              # hash table doesn't exist
            self._hash_tbl[hv] = Bucket()
        bucket = self._hash_tbl[hv]
        bucket._setitem(k, v)

    def _delitem(self, k):                          # delete item
        hv = self._hash_value(k)                    # hasg value
        bucket = self._hash_tbl[hv]
        bucket._delitem(k)                          # delete item
        self._num_entry -= 1

    def __str__(self):                              # print out string
        s = ''
        for h in range(len(self._hash_tbl)):
            bucket = self._hash_tbl[h]
            if bucket is not None:
                s += "bucket[{:2d}] : ".format(h)
                for item in bucket:
                    s += str(item) + ", "
                s += "\n "
        return s


def CyclicShiftHashCode(str_key):                       # str_key is string
    mask = (1 << 32) - 1                # 32bit 0b11111111 11111111 11111111 11111111
    h = 0
    for ch in str_key:
        h = (h << 5 & mask) | (h >> 27)  # cyclic shift hash code, h 초기값 0
        # ch=> (k, i, m), (H, o, n, g)...
        h += ord(ch)
    return h

