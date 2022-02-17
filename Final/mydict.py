class mydict:
    size = 16
    def __init__(self):
        # create a list of empty lists of size 16
        self.data = [[] for i in range(self.size)]

    def _find(self,key):
        #check if list is empty or has no length
        index = hash(key) % (self.size)
        sublist = self.data[index]
        if len(sublist) == 0:
            return (sublist, None)
        else:
            index = 0
            for i in sublist:
                if i[0] == key:
                    return (sublist,index)
                else:
                    #does not exist already
                    index += 1
            return (sublist, None)

    def __getitem__(self,key):
        # if item matching key is dictionary, 
        # return the value otherwise raise KeyError
        # must use _find
        index = self._find(key)
        if index[1] == None:
            #does not exist
            raise KeyError
        else:
            return index[0][index[1]][1]

    def __setitem__(self,key,value):
        # Set value of item with key, or insert item 
        # with key in dictionary
        # must use _find
        index = self._find(key)
        if index[1] == None:
            #does not exist empty list
            index[0].append([key, value])
        else:
            index[0][index[1]] = [key, value]

                
    def __contains__(self,key):
        # if item matching key is in dictionary, 
        # return True otherwise return False
        # must use _find
        index = self._find(key)
        if index[1] == None:
            return False
        else:
            return True
   
    def keys(self):
        # return a list of the keys in the dictionary
        keys = []
        for i in range(self.size):
            if self.data[i] != []:
                for j in range(len(self.data[i])):
                    keys.append(self.data[i][j][0])
        return keys

    def values(self):
        # return a list of values in dictionary
        vals = []
        for i in range(self.size):
            if self.data[i] != []:
                for j in range(len(self.data[i])):
                    vals.append(self.data[i][j][1])
        return vals

    def items(self):
        s = []
        # return a list of items [(key,value),...]
        keys = self.keys()
        values = self.values()
        for i in range(len(keys)):
            s.append((keys[i],values[i]))
        return s
            
    def pop(self,key):
        # remove item with key from dictionary and 
        # return corresponding value
        # raise KeyError if item doesn't exist
        # must use _find
        index = self._find(key)
        if self.__contains__(key) == True:
            val = index[0][0][1]
            index[0].remove(index[0][0])
            return val
        else:
            raise KeyError

    def __delitem__(self,key):
        # remove item with key from dictionary
        # raise KeyError if item doesn't exist
        # returns None
        index = self._find(key)
        if self.__contains__(key) == True:
            index[0].remove(index[0][0])
            return None
        else:
            raise KeyError
        

    def __len__(self):
        # return the number of elements in the dictionary
        return len(self.items())

    def __str__(self):
        items = self.items()
        str = "{ "
        for i in range(len(items)):
            if i == len(items) - 1:
                str += f"{items[i][0]} : {items[i][1]}"
            else:
                str += f"{items[i][0]} : {items[i][1]}, "
        str += " }"
        return str


if __name__ == "__main__":
    d = mydict()
    d[1] = 33
    print(d[1])
    try:
        print(d[2])
    except KeyError:
        print("2 is not a valid key")
    d['a'] = 33
    d['b'] = 44
    print(d.keys())
    print(d.values())
    print(d.items())
    print(f'length {len(d)}')
    print(d)
    print('a' in d)
    print('xx' in d)
    print(d.pop('a'))
    print('a' in d)
    print(d['b'])
    del d['b']
    try:
        print(d['b'])
    except KeyError:
        print('b is not in d')
    
    e1 = None
    try:
        d2 = {}
        d2[['a']] = 33
    except Exception as e:
        e1 = e
    
    e2 = None
    try:
        d[['a']] = 33
    except Exception as e:
        e2 = e
        print(type(e).__name__,e)

    assert type(e1) is type(e2) and e1.args == e2.args