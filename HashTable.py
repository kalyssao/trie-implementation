
#A hashtable class which is used to store the Name as key and
#the ID numbers of students as values

import random
class HashTable:
    def __init__(self):
        self.size = 1000
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0
        self.key = 0

    def put(self,key,data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            nextslot = self.rehash(hashvalue, len(self.slots))

            while self.slots[nextslot] != None and \
                          self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]= key
                self.data[nextslot]= data
#---------------------------------------------------------------------
   #Hashfunction method and the generateID were introduced to the hash table class

    def hashfunction(self,key,size):
        if type(key) == int:
            return key % size
        else:
            str_key = list(key)
            sum = 0
            a = 1
            for i in str_key:
                sum += ord(i)* a
                a += 1
            return sum % size

    def generateID(self, classYear):
        #Generating a four digit random number
        number = random.randint(1111, 9999)
        #Creating the ID
        ID = str(number) + str(classYear)

        #If the ID is already present in the HashTable,
        #A new ID is generated
        #self.count is updated each time, a new ID is generated
        while ID in self.data:
            number = random.randint(0000,9999)
            ID = str(number) + str(classYear)
            self.count += 1

        return ID 

#---------------------------------------------------------------------

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        
        while self.slots[position] != None and  \
                           not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

            if position == startslot:
                stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)